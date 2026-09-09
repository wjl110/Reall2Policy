# 实验台账总览

最后更新：2026-09-10 02:50

| 区 | 文件 |
|----|------|
| 当前状态 | [CURRENT.md](CURRENT.md) |
| 硬件节点 | [nodes/hardware.md](nodes/hardware.md) |
| 踩坑 | [pitfalls/INDEX.md](pitfalls/INDEX.md) |
| 会话 | [sessions/](sessions/) |

## 实验

| 日期 | 实验 | 状态 | 数据 / 产物 | 文件 |
|------|------|------|-------------|------|
| 2026-09-08 | Windows 环境安装与 verify | 成功 | `logs/verification.json` | [experiments/2026-09-08_env-verify.md](experiments/2026-09-08_env-verify.md) |
| 2026-09-10 | 校准 + 遥操打通 | 成功 | `calibration/` Leader COM3 / Follower COM4 | [experiments/2026-09-10_calibrate-teleop.md](experiments/2026-09-10_calibrate-teleop.md) |
| 2026-09-10 | 首次录制试跑 | 部分成功 | `so101_first_test_*`（正式用 `..._003232`） | [experiments/2026-09-10_first-record.md](experiments/2026-09-10_first-record.md) |
| 2026-09-10 | 抓放 20 集采集 | 成功 | `so101_pick_place_20260910_011033` 20ep / 9000f | [experiments/2026-09-10_pick-place-20.md](experiments/2026-09-10_pick-place-20.md) |
| 2026-09-10 | ACT 训练 100K | 进行中 | ckpt `020000`，resume 中约 22K | [experiments/2026-09-10_act-train.md](experiments/2026-09-10_act-train.md) |
| 2026-09-10 | 建立实验台账 Skill | 成功 | `lab-log/` + `.cursor/skills/reall2policy-lab-log` | [experiments/2026-09-10_lab-log-skill.md](experiments/2026-09-10_lab-log-skill.md) |

## 数据集一览（`data/local/`）

| 目录 | episodes | frames | 用途 |
|------|----------|--------|------|
| so101_first_test_20260910_002706 | 1 | 300 | 试录残留 |
| so101_first_test_20260910_002752 | 1 | 300 | 试录残留 |
| so101_first_test_20260910_003232 | 1 | 300 | 首次完整试录（replay 用这个） |
| so101_pick_place | 0 | 0 | 空壳（同名冲突残留） |
| so101_pick_place_20260910_010322 | 0 | 0 | 空壳 |
| so101_pick_place_20260910_010406 | 0 | 0 | 空壳 |
| so101_pick_place_20260910_010431 | 1 | 269 | 正式采集中断 |
| so101_pick_place_20260910_010511 | 1 | 319 | 正式采集中断 |
| so101_pick_place_20260910_010721 | 6 | 2700 | 正式采集未满 20 |
| **so101_pick_place_20260910_011033** | **20** | **9000** | **当前训练数据** |

## 关键踩坑（详见 pitfalls）

- P001 串口被占 / `openPort` 失败
- P002 Hugging Face 401，必须 `push_to_hub=false`
- P003 同名数据集被改成时间戳目录
- P004 夹爪 id=6 Overload
- P005 WinError 1314 无法创建 `checkpoints/last` 符号链接
- P006 本地视频训练要用 `video_backend=pyav`
