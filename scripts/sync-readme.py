#!/usr/bin/env python3
"""Sync README tagline, footnote, and progress table from lab-log/metrics.json."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS_PATH = ROOT / "lab-log" / "metrics.json"
README_PATH = ROOT / "README.md"
DATASET_INFO = ROOT / "data" / "local" / "so101_pick_place_20260910_011033" / "meta" / "info.json"

MARKERS = {
    "tagline": ("readme:tagline:start", "readme:tagline:end"),
    "footnote": ("readme:footnote:start", "readme:footnote:end"),
    "progress": ("readme:progress:start", "readme:progress:end"),
}


def load_metrics() -> dict:
    if not METRICS_PATH.is_file():
        raise SystemExit(f"Missing metrics file: {METRICS_PATH}")
    return json.loads(METRICS_PATH.read_text(encoding="utf-8"))


def warn_if_episodes_mismatch(readme: dict) -> None:
    if not DATASET_INFO.is_file():
        return
    info = json.loads(DATASET_INFO.read_text(encoding="utf-8"))
    disk_eps = info.get("total_episodes")
    json_eps = readme.get("demonstrations")
    if disk_eps is not None and json_eps is not None and disk_eps != json_eps:
        print(
            f"warning: metrics.readme.demonstrations={json_eps} "
            f"but info.json total_episodes={disk_eps}",
            file=sys.stderr,
        )


def build_tagline(readme: dict) -> str:
    demos = readme["demonstrations"]
    target = readme["demonstrations_target"]
    policy = readme.get("headline_policy", "ACT")
    step = readme.get("headline_step", "").strip()
    policy_bit = f"{policy} {step}" if step else policy
    return (
        f"`{demos} demonstrations (target {target}) · {policy_bit} · "
        "Diffusion Policy · SmolVLA · OOD Generalization`"
    )


def build_footnote(readme: dict) -> str:
    text = readme.get(
        "footnote",
        "进度由 `lab-log/metrics.json` 生成；实验数字以 `experiments/INDEX.md` 与 `results/` 为准，未测完不写成功率。",
    )
    return f"> {text}"


def build_progress_table(week_rows: list[dict]) -> str:
    lines = ["| 周 | 状态 |", "|---|---|"]
    for row in week_rows:
        lines.append(f"| {row['label']} | {row['status']} |")
    return "\n".join(lines)


def replace_block(text: str, block: str, content: str) -> str:
    start, end = MARKERS[block]
    pattern = rf"(<!-- {re.escape(start)} -->)\s*[\s\S]*?\s*(<!-- {re.escape(end)} -->)"
    new_text, count = re.subn(pattern, rf"\1\n{content}\n\2", text, count=1)
    if count != 1:
        raise SystemExit(f"Missing or duplicate README marker block: {block}")
    return new_text


def main() -> int:
    metrics = load_metrics()
    readme = metrics.get("readme")
    if not readme:
        raise SystemExit("metrics.json missing 'readme' section")
    if "week_rows" not in readme:
        raise SystemExit("metrics.json readme.week_rows is required")

    warn_if_episodes_mismatch(readme)

    text = README_PATH.read_text(encoding="utf-8")
    text = replace_block(text, "tagline", build_tagline(readme))
    text = replace_block(text, "footnote", build_footnote(readme))
    text = replace_block(text, "progress", build_progress_table(readme["week_rows"]))
    README_PATH.write_text(text, encoding="utf-8")
    print(f"Synced {README_PATH.relative_to(ROOT)} from {METRICS_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
