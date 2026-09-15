#!/usr/bin/env python3
"""Poll DP / train job. Writes lab-log/train-live.json + dp-countdown.html."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import threading
import time
import webbrowser
from datetime import datetime, timedelta, timezone
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_JOB = "dp_so101_v1"
DEFAULT_CKPT = ROOT / "outputs" / "train" / "dp_so101_v1" / "checkpoints"
OUT_JSON = ROOT / "lab-log" / "train-live.json"
OUT_JS = ROOT / "lab-log" / "train-live.js"
OUT_HTML = ROOT / "lab-log" / "dp-countdown.html"
HTTP_PORT = 8765
STEPS_TARGET = 100_000
CKPT_EVERY = 20_000
TZ = timezone(timedelta(hours=8))
TERMINALS = Path(
    os.environ.get(
        "CURSOR_TERMINALS",
        r"C:\Users\18431\.cursor\projects\d-SO-ARM101\terminals",
    )
)

TQDM_RE = re.compile(
    r"(?P<step>\d+)/100000 \[(?P<elapsed>[0-9:]+)<(?P<remain>[^,]+), +"
    r"(?P<rate>[\d.]+)(?P<unit>s/step|step/s)\]"
)
INFO_RE = re.compile(
    r"INFO (?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) .*?step:(?P<step>\S+) "
    r".*?loss:(?P<loss>[\d.]+) .*?step_s:(?P<step_s>[\d.]+)"
)
WEEKDAY = "一二三四五六日"


def now_local() -> datetime:
    return datetime.now(TZ)


def parse_step_token(token: str) -> int | None:
    token = token.strip()
    if token.endswith("K") or token.endswith("k"):
        try:
            return int(float(token[:-1]) * 1000)
        except ValueError:
            return None
    if token.isdigit():
        return int(token)
    return None


def parse_hms(text: str) -> float | None:
    parts = text.strip().split(":")
    try:
        nums = [int(p) for p in parts]
    except ValueError:
        return None
    if len(nums) == 3:
        return nums[0] * 3600 + nums[1] * 60 + nums[2]
    if len(nums) == 2:
        return nums[0] * 60 + nums[1]
    return None


def parse_log_text(text: str) -> dict:
    out: dict = {}
    last_bar = None
    for m in TQDM_RE.finditer(text):
        last_bar = m
    if last_bar:
        step = int(last_bar.group("step"))
        rate = float(last_bar.group("rate"))
        unit = last_bar.group("unit")
        sec = rate if unit == "s/step" else (1.0 / rate if rate else None)
        out["step"] = step
        out["sec_per_step"] = sec
        out["tqdm_remain"] = last_bar.group("remain").strip()
        out["tqdm_elapsed"] = last_bar.group("elapsed").strip()
    last_info = None
    for m in INFO_RE.finditer(text):
        last_info = m
    if last_info:
        out["loss"] = float(last_info.group("loss"))
        out["info_step_s"] = float(last_info.group("step_s"))
        out["info_ts"] = last_info.group("ts")
        if "step" not in out:
            info_step = parse_step_token(last_info.group("step"))
            if info_step is not None:
                out["step"] = info_step
            out["sec_per_step"] = out["info_step_s"]
    return out


def latest_train_log(job: str) -> dict:
    if not TERMINALS.is_dir():
        return {}
    newest: tuple[float, dict] | None = None
    for path in TERMINALS.glob("*.txt"):
        try:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if job not in raw:
            continue
        parsed = parse_log_text(raw[-400_000:])
        if "step" not in parsed:
            continue
        mtime = path.stat().st_mtime
        if newest is None or mtime > newest[0]:
            newest = (mtime, parsed)
    return newest[1] if newest else {}


def numeric_ckpts(ckpt_root: Path) -> list[tuple[int, Path, datetime]]:
    rows = []
    if not ckpt_root.is_dir():
        return rows
    for p in ckpt_root.iterdir():
        if p.is_dir() and p.name.isdigit():
            step = int(p.name)
            stamp = datetime.fromtimestamp(p.stat().st_mtime, TZ)
            rows.append((step, p, stamp))
    return sorted(rows)


def gpu() -> tuple[int | None, int | None, int | None, float | None]:
    try:
        out = subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=utilization.gpu,memory.used,memory.total,power.draw",
                "--format=csv,noheader,nounits",
            ],
            text=True,
            timeout=8,
        ).strip()
        parts = [x.strip() for x in out.split(",")]
        util, used, total = [int(float(x)) for x in parts[:3]]
        watts = float(parts[3]) if len(parts) > 3 else None
        return util, used, total, watts
    except (OSError, subprocess.SubprocessError, ValueError):
        return None, None, None, None


def train_alive(job: str) -> bool:
    try:
        out = subprocess.check_output(
            [
                "powershell",
                "-NoProfile",
                "-Command",
                "Get-CimInstance Win32_Process | "
                "Where-Object { $_.CommandLine -like '*lerobot-train*' -and $_.CommandLine -like '*"
                + job
                + "*' } | "
                "Select-Object -ExpandProperty ProcessId",
            ],
            text=True,
            timeout=10,
        )
        return bool(out.strip())
    except (OSError, subprocess.SubprocessError):
        return False


def fmt_hms(seconds: float | None) -> str:
    if seconds is None or seconds < 0:
        return "—"
    total = int(round(seconds))
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def fmt_finish(when: datetime | None) -> str:
    if when is None:
        return "—"
    wd = WEEKDAY[when.weekday()]
    return when.strftime(f"%m/%d 周{wd} %H:%M")


def next_ckpt(step: int) -> int | None:
    nxt = ((step // CKPT_EVERY) + 1) * CKPT_EVERY
    if nxt > STEPS_TARGET:
        return None
    return nxt


def snapshot(job: str, ckpt_root: Path) -> dict:
    t = now_local()
    ckpts = numeric_ckpts(ckpt_root)
    last_step = ckpts[-1][0] if ckpts else 0
    last_time = ckpts[-1][2] if ckpts else None
    log = latest_train_log(job)
    step = max(last_step, int(log.get("step") or 0))
    sec = log.get("sec_per_step")
    if sec is None and log.get("info_step_s"):
        sec = log["info_step_s"]
    remain_steps = max(0, STEPS_TARGET - step)
    eta_s = remain_steps * sec if sec else None
    finish = t + timedelta(seconds=eta_s) if eta_s is not None else None
    nxt = next_ckpt(step)
    nxt_eta = (nxt - step) * sec if nxt and sec else None
    util, used, total, watts = gpu()
    alive = train_alive(job)
    healthy = bool(alive and (util is None or util >= 15))
    return {
        "job": job,
        "updated": t.strftime("%Y-%m-%d %H:%M:%S"),
        "alive": alive,
        "healthy": healthy,
        "gpu_util_pct": util,
        "vram_used_mb": used,
        "vram_total_mb": total,
        "gpu_watts": watts,
        "ckpt_steps": [s for s, _, _ in ckpts],
        "last_ckpt": last_step,
        "last_ckpt_time": last_time.strftime("%Y-%m-%d %H:%M:%S") if last_time else None,
        "step": step,
        "target_step": STEPS_TARGET,
        "progress_pct": round(100.0 * step / STEPS_TARGET, 2),
        "sec_per_step": round(sec, 3) if sec else None,
        "loss": log.get("loss"),
        "eta_s": int(round(eta_s)) if eta_s is not None else None,
        "eta_hms": fmt_hms(eta_s),
        "finish_at": finish.strftime("%Y-%m-%d %H:%M:%S") if finish else None,
        "finish_label": fmt_finish(finish),
        "next_ckpt": nxt,
        "next_ckpt_hms": fmt_hms(nxt_eta),
        "note": "step 来自训练日志 tqdm；倒计时 = 剩余步 × 当前秒/步。",
    }


def write_live_js(data: dict) -> None:
    payload = json.dumps(data, ensure_ascii=False)
    OUT_JS.write_text(f"window.TRAIN_LIVE = {payload};\n", encoding="utf-8")


class _LabLogHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / "lab-log"), **kwargs)

    def log_message(self, *_args) -> None:
        return

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


def start_http(port: int) -> int | None:
    for candidate in range(port, port + 8):
        try:
            httpd = ThreadingHTTPServer(("127.0.0.1", candidate), _LabLogHandler)
        except OSError:
            continue
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        return candidate
    return None


def emit(data: dict) -> None:
    OUT_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    write_live_js(data)
    print(
        f"{data['updated']}  step={data['step']}  {data['sec_per_step']}s/step  "
        f"eta={data['eta_hms']}  finish={data['finish_label']}  "
        f"gpu={data['gpu_util_pct']}%  alive={data['alive']}",
        flush=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", default=DEFAULT_JOB)
    parser.add_argument("--ckpt-root", default=str(DEFAULT_CKPT))
    parser.add_argument("--interval", type=float, default=2.0)
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--port", type=int, default=HTTP_PORT)
    parser.add_argument("--open", action="store_true")
    args = parser.parse_args()
    ckpt_root = Path(args.ckpt_root)
    if not OUT_HTML.is_file():
        raise SystemExit(f"缺少大屏页：{OUT_HTML}")
    bound = None if args.once else start_http(args.port)
    if bound:
        url = f"http://127.0.0.1:{bound}/dp-countdown.html"
        print(f"DASHBOARD={url}", flush=True)
        if args.open:
            webbrowser.open(url)
    while True:
        emit(snapshot(args.job, ckpt_root))
        if args.once:
            return
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
