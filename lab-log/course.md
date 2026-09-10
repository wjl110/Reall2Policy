# 课表学习实践跟踪

课表原文（抄命令）：[`docs/COURSE.md`](../docs/COURSE.md)  
实验数字：[`experiments/INDEX.md`](../experiments/INDEX.md)  
更新：2026-09-11 01:13

## 当前焦点

**W3 E02 重训进行中（~58K/100K，ckpt 20K/40K）。**  
GPU 占用：不要录制、不要 resume 同一数据集。不要并行 DP/VLA。

本周实践 vs 课表：W2 50/100 已齐；E02 训至 ~58K；W4 rollout + Demo GIF 已上 README。总目标 100 等 E02 结束后再补。

## 总进度

| 周 | 课表目标 | 实践状态 | 证据 | 差距 |
|----|----------|----------|------|------|
| W0 环境 | verify | **完成** | `logs/verification.json` | 无 |
| W1 遥操 | 校准 + teleop | **完成** | `calibration/` COM3/COM4 | 无 |
| W2 数据 | 100 episodes | **进行中 50/100** | `so101_pick_place_20260910_011033` | 缺 50（E03）；E02 可训 |
| W3 ACT | E01/E02/E03 各 100K | **E01 完成**；**E02 ~58K/100K**；E03 未开始 | E02 ckpt 20K/40K | 等训完再 +50→E03 |
| W4 拔 Leader | 真机 rollout + Demo | **进行中** | rollout OK；README Demo GIF | 缺 `assets/demo.mp4` |
| W5–6 Eval/OOD | 填评测表 | 未开始 | 模板 `results/eval_template.md` | — |
| W7 Flywheel | hard cases + ACT-v2 | 未开始 | — | 依赖 W6 最差条件 |
| W8 ACT vs DP | 同数据对比 | 未开始 | 模板 `results/act_vs_dp.md` | 禁止现在并行 |
| W9–10 SmolVLA | 语言指令 | 未开始 | — | 禁止现在并行 |
| W11 World Model | 预测实验 | 未开始 | — | **不到该周不要做** |
| W12 作品集 | GitHub + Demo | 进行中 | https://github.com/wjl110/Reall2Policy | Demo GIF 已上；README 同步机制已建 |

## 按周实践记录

### W0 环境

- 课表：`verify.cmd`、`lerobot-find-port`
- 实际：2026-09-08 软件自检通过
- 差距：无

### W1 遥操

- 课表：calibrate follower/leader + teleoperate
- 实际：2026-09-10 校准文件已生成，遥操已通；踩过 P001 串口、P004 夹爪过载
- 差距：无

### W2 数据

- 课表：100 ep，覆盖 Left/Center/Right/Near/Far；正常光+略变光；Approach A/B/C
- 实际：2026-09-10 先 20 条（每集 **15s** / 450 帧）；Esc 停在 25；23:17 **resume 完成 50 ep / 27000 帧**（后 30 条每集 20s）
- 差距：总目标 100 还缺 50；位置/光照网格是否铺开未逐条核
- 下次实践：E02 训完后再 `num_episodes=50` 加到 100

### W3 ACT

- 课表：E01(20) → E02(50) → E03(100)
- 实际：E01 01:21 启动 → 20K P005 → resume → 05:03 **100K 完成**，loss≈0.051。E02 第一次 614 因 P012 崩；23:28 重训已过 614，~4K loss≈0.69
- 差距：E02 未完；E03 未开始

### W4 拔 Leader

- 课表：rollout + `assets/demo.mp4`
- 实际：2026-09-10 用 `checkpoints/100000` 做 `lerobot-rollout`；折叠态失败（P010），工作姿态下用户确认完全 OK
- 差距：未录像 Demo；未做 30–50 次计数（那是 W5–6）

### W5–W12

W5 起尚未按评测表实践。

## 偏离 / 拦截

| 日期 | 事项 | 处理 |
|------|------|------|
| 2026-09-10 | 训练读盘期间不可 resume 同一数据集 | 已解除（E01 结束） |
| 2026-09-10 | W4 rollout 在 W2 补满前做了 | 允许：E01 权重已可用；下一步仍回 W2 补采，不跳去 DP/VLA |
| 2026-09-10 | E02 在补采视频落盘前开训 | P012 崩在 614；视频现已齐，从头重训 |

## 每周节奏（对照用）

课表：一/二工程，三/四算法，五记实验，六日大实验。  
2026-09-10（周四）：W3 结束 + W4 初验；晚间进入 W2 补采。
