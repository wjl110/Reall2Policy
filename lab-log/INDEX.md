# 实验台账总览

最后更新：2026-09-10 03:22


| 区    | 文件                                                               |
| ---- | ---------------------------------------------------------------- |
| 当前状态 | [CURRENT.md](CURRENT.md)                                         |
| 课表实践 | [course.md](course.md)（对照 [`docs/COURSE.md`](../docs/COURSE.md)） |
| 图表 | [charts.md](charts.md) · [metrics.json](metrics.json) |
| 硬件节点 | [nodes/hardware.md](nodes/hardware.md)                           |
| 踩坑   | [pitfalls/INDEX.md](pitfalls/INDEX.md)                           |
| 会话   | [sessions/](sessions/)                                           |


## 实验


| 日期         | 实验                   | 状态   | 数据 / 产物                                            | 文件                                                                                       |
| ---------- | -------------------- | ---- | -------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 2026-09-08 | Windows 环境安装与 verify | 成功   | `logs/verification.json`                           | [experiments/2026-09-08_env-verify.md](experiments/2026-09-08_env-verify.md)             |
| 2026-09-10 | 校准 + 遥操打通            | 成功   | `calibration/` Leader COM3 / Follower COM4         | [experiments/2026-09-10_calibrate-teleop.md](experiments/2026-09-10_calibrate-teleop.md) |
| 2026-09-10 | 首次录制试跑               | 部分成功 | 目录已于 03:19 清理（历史见实验文件）                      | [experiments/2026-09-10_first-record.md](experiments/2026-09-10_first-record.md)         |
| 2026-09-10 | 抓放 20 集采集            | 成功   | `so101_pick_place_20260910_011033` 20ep / 9000f    | [experiments/2026-09-10_pick-place-20.md](experiments/2026-09-10_pick-place-20.md)       |
| 2026-09-10 | ACT 训练 100K          | 进行中  | ckpt `020000`+`040000`，约 40K                        | [experiments/2026-09-10_act-train.md](experiments/2026-09-10_act-train.md)               |
| 2026-09-10 | 建立实验台账 Skill         | 成功   | `lab-log/` + `.cursor/skills/reall2policy-lab-log` | [experiments/2026-09-10_lab-log-skill.md](experiments/2026-09-10_lab-log-skill.md)       |
| 2026-09-10 | 12 周课表落地             | 成功   | `docs/COURSE.md` + configs/experiments/results     | [experiments/2026-09-10_course-setup.md](experiments/2026-09-10_course-setup.md)         |




## 数据集一览（`data/local/`）


| 目录                                   | episodes | frames   | 用途                 |
| ------------------------------------ | -------- | -------- | ------------------ |
| **so101_pick_place_20260910_011033** | **20**   | **9000** | **当前唯一本地数据 / 训练中** |

2026-09-10 03:19 用户删除试录、空壳、中断目录（`so101_first_test_*`、`so101_pick_place` 空壳、`..._010322`～`..._010721`）。




## 关键踩坑（详见 pitfalls）

- P001 串口被占 / `openPort` 失败
- P002 Hugging Face 401，必须 `push_to_hub=false`
- P003 同名数据集被改成时间戳目录
- P004 夹爪 id=6 Overload
- P005 WinError 1314 无法创建 `checkpoints/last` 符号链接
- P006 本地视频训练要用 `video_backend=pyav`

