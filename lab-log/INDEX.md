# 实验台账总览

最后更新：2026-09-15 08:34


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
| 2026-09-10 | 抓放补采到 50 集           | 成功   | 同 root **50ep / 27000f**                          | [experiments/2026-09-10_pick-place-50.md](experiments/2026-09-10_pick-place-50.md)       |
| 2026-09-12 | 抓放补采到 100 集         | 成功   | 同 root **100ep / 65100f**；file-003/004 已落盘 | [experiments/2026-09-12_pick-place-100.md](experiments/2026-09-12_pick-place-100.md)     |
| 2026-09-10 | ACT 训练 100K          | 成功   | ckpt `020000`/`040000`/`100000`，loss≈0.051            | [experiments/2026-09-10_act-train.md](experiments/2026-09-10_act-train.md)               |
| 2026-09-10 | ACT E02 训练（50 ep）  | 成功   | ckpt 20/40/60/80/100K，loss≈0.065 @100K                  | [experiments/2026-09-10_act-train-e02.md](experiments/2026-09-10_act-train-e02.md)       |
| 2026-09-12 | ACT E03 训练（100 ep） | 成功   | ckpt 20/40/60/80/100K，loss 0.168 @100K；P014 后 resume | [experiments/2026-09-12_act-train-e03.md](experiments/2026-09-12_act-train-e03.md)       |
| 2026-09-10 | E01 真机 rollout       | 成功   | 姿态对齐后抓放 OK；折叠态抖动见 P010                   | [experiments/2026-09-10_rollout-e01.md](experiments/2026-09-10_rollout-e01.md)           |
| 2026-09-11 | E02 真机 rollout       | 部分成功 | 第一轮抓放 OK；回折叠后第二轮卡死（P013） | [experiments/2026-09-11_rollout-e02.md](experiments/2026-09-11_rollout-e02.md)           |
| 2026-09-12 | E03 真机 rollout       | 完成 | `assets/demo.mp4` 已齐；W4 过 | [experiments/2026-09-12_rollout-e03.md](experiments/2026-09-12_rollout-e03.md)           |
| 2026-09-12 | E03 IID 计次           | 完成 | 37/90 (41%)；第5轮6–15取抓不正常已确认 | [experiments/2026-09-12_eval-iid.md](experiments/2026-09-12_eval-iid.md)                 |
| 2026-09-12 | E03 Position OOD       | 失败 | 0/90；离开夹下找不到（P016） | [experiments/2026-09-12_eval-position-ood.md](experiments/2026-09-12_eval-position-ood.md) |
| 2026-09-12 | E03 Object OOD         | 失败 | 0/90；半透明盒；第6轮开合反向 | [experiments/2026-09-12_eval-object-ood.md](experiments/2026-09-12_eval-object-ood.md)     |
| 2026-09-12 | E03 Lighting OOD       | 部分 | 1/90；多为触碰；右侧一次抓取 | [experiments/2026-09-12_eval-lighting-ood.md](experiments/2026-09-12_eval-lighting-ood.md) |
| 2026-09-12 | E03 Background OOD     | 同批 | 与 Lighting 同一批 1/90，不另跑 | [experiments/2026-09-12_eval-background-ood.md](experiments/2026-09-12_eval-background-ood.md) |
| 2026-09-12 | E03 Camera Shift       | 部分 | 19/90；夹下预张爪；换侧斜前 | [experiments/2026-09-12_eval-camera-shift.md](experiments/2026-09-12_eval-camera-shift.md) |
| 2026-09-12 | W7 DAgger 第一趟       | 失败 | 18min / 7 次纠正 / 0 ep（P018） | [experiments/2026-09-12_dagger-collect.md](experiments/2026-09-12_dagger-collect.md)       |
| 2026-09-13 | W7 DAgger dagger2      | 成功 | 14 ep / 37494 帧 / 61 纠正 | [experiments/2026-09-13_dagger2-collect.md](experiments/2026-09-13_dagger2-collect.md)     |
| 2026-09-13 | W7 ACT-v2 训练         | 成功 | `100000` @05:09；100K loss 无日志 | [experiments/2026-09-13_act-train-v2.md](experiments/2026-09-13_act-train-v2.md)           |
| 2026-09-13 | W7 ACT-v2 复测         | 进行中 | IID 0/15；Pos 0/15 | [experiments/2026-09-13_eval-act-v2.md](experiments/2026-09-13_eval-act-v2.md)             |
| 2026-09-13 | W7 飞轮 v3 方案         | 已确认 | 先采 dagger3 | [experiments/2026-09-13_flywheel-v3-plan.md](experiments/2026-09-13_flywheel-v3-plan.md)   |
| 2026-09-13 | W7 DAgger dagger3      | 成功 | 11 ep / 73 纠正 | [experiments/2026-09-13_dagger3-collect.md](experiments/2026-09-13_dagger3-collect.md)     |
| 2026-09-13 | W7 ACT-v3 训练         | 成功 | 111 ep 混合集；**100000 @15:41** | [experiments/2026-09-13_act-train-v3.md](experiments/2026-09-13_act-train-v3.md)           |
| 2026-09-13 | W7 ACT-v3 复测         | 成功 | IID 8/90；Pos **13/90** | [experiments/2026-09-13_eval-act-v3.md](experiments/2026-09-13_eval-act-v3.md)             |
| 2026-09-13 | W8 Diffusion 训练      | 成功 | 同一 100 ep；**100000 @08:34** | [experiments/2026-09-13_dp-train.md](experiments/2026-09-13_dp-train.md)                   |
| 2026-09-13 | Hub 开放数据适配       | 结论   | 能加载；不能混本机 ACT；W9 再用 smolvla_base | [experiments/2026-09-13_hub-dataset-adapt.md](experiments/2026-09-13_hub-dataset-adapt.md) |
| 2026-09-13 | SmolVLA 路线           | 结论   | W9 微调 base，不走从零+20K；现在不开 | [experiments/2026-09-13_smolvla-route.md](experiments/2026-09-13_smolvla-route.md) |
| 2026-09-13 | 官方提效对照           | 结论   | 慢在重复满训；Hub ACT 不可复用；W9 微调 + 下轮接着训 | [experiments/2026-09-13_hf-efficiency.md](experiments/2026-09-13_hf-efficiency.md) |
| 2026-09-10 | 建立实验台账 Skill         | 成功   | `lab-log/` + `.cursor/skills/reall2policy-lab-log` | [experiments/2026-09-10_lab-log-skill.md](experiments/2026-09-10_lab-log-skill.md)       |
| 2026-09-10 | 12 周课表落地             | 成功   | `docs/COURSE.md` + configs/experiments/results     | [experiments/2026-09-10_course-setup.md](experiments/2026-09-10_course-setup.md)         |




## 数据集一览（`data/local/`）


| 目录                                   | episodes | frames   | 用途                 |
| ------------------------------------ | -------- | -------- | ------------------ |
| **so101_pick_place_20260910_011033** | **100**   | **65100** | **E03 数据已齐** |
| **rollout_so101_dagger2** | **14** | **37494** | **W7 DAgger v2（含 intervention）** |
| **rollout_so101_dagger3** | **11** | **33623** | **W7 DAgger v3（73 纠正）** |
| **so101_v3_mix** | **111** | **98723** | **100 专家 + dagger3（已去 intervention）** |

2026-09-10 03:19 用户删除试录、空壳、中断目录（`so101_first_test_*`、`so101_pick_place` 空壳、`..._010322`～`..._010721`）。




## 关键踩坑（详见 pitfalls）

- P001 串口被占 / `openPort` 失败
- P002 Hugging Face 401，必须 `push_to_hub=false`
- P003 同名数据集被改成时间戳目录
- P004 夹爪 id=6 Overload
- P005 WinError 1314 无法创建 `checkpoints/last` 符号链接
- P006 本地视频训练要用 `video_backend=pyav`
- P010 折叠起始姿态 rollout 只抖动，必须先摆到录制姿态
- P011 录制 Esc/`q` 会整段退出（含 Rerun 窗口）
- P012 补采 mp4 未落盘就开训，DataLoader 找不到 file-002
- P013 抓放成功后回折叠，第二轮卡死抖动
- P019 ACT-v2 夹后伸缩、不放置
- P020 ACT-v3 夹前再往前推
- P021 训 Diffusion 缺 `lerobot[diffusion]`

