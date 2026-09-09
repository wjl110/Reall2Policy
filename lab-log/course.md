# 课表学习实践跟踪

课表原文（抄命令）：[`docs/COURSE.md`](../docs/COURSE.md)  
实验数字：[`experiments/INDEX.md`](../experiments/INDEX.md)  
更新：2026-09-10 03:03

## 当前焦点

**W3 E01 ACT 在跑，同时 W2 数据只有 20/100。**  
课表要求：训练结束前不要补采同一份数据，不要并行 DP/VLA。

本周实践 vs 课表：正在练 W3 算法（续训）；W2 采集未补；W4 真机未开始。

## 总进度

| 周 | 课表目标 | 实践状态 | 证据 | 差距 |
|----|----------|----------|------|------|
| W0 环境 | verify | **完成** | `logs/verification.json` | 无 |
| W1 遥操 | 校准 + teleop | **完成** | `calibration/` COM3/COM4 | 无 |
| W2 数据 | 100 episodes | **进行中 20/100** | `so101_pick_place_20260910_011033` | 缺 80；+30 再 +50 须等 E01 结束 |
| W3 ACT | E01/E02/E03 各 100K | **进行中 E01 ~30K/100K** | `outputs/train/act_so101_pick_place` ckpt 020000 | E02/E03 未开始 |
| W4 拔 Leader | 真机 rollout + Demo | 未开始 | — | 等 E01 更好 ckpt |
| W5–6 Eval/OOD | 填评测表 | 未开始 | 模板 `results/eval_template.md` | — |
| W7 Flywheel | hard cases + ACT-v2 | 未开始 | — | 依赖 W6 最差条件 |
| W8 ACT vs DP | 同数据对比 | 未开始 | 模板 `results/act_vs_dp.md` | 禁止现在并行 |
| W9–10 SmolVLA | 语言指令 | 未开始 | — | 禁止现在并行 |
| W11 World Model | 预测实验 | 未开始 | — | **不到该周不要做** |
| W12 作品集 | GitHub + Demo | 未开始 | 待 `gh auth login` | — |

## 按周实践记录

### W0 环境

- 课表：`verify.cmd`、`lerobot-find-port`
- 实际：2026-09-08 软件自检通过
- 差距：无

### W1 遥操

- 课表：calibrate follower/leader + teleoperate
- 实际：2026-09-10 校准文件已生成，遥操已通；踩过 P001 串口、P004 夹爪过载
- 差距：无（复检命令课表里仍保留）

### W2 数据

- 课表：100 ep，覆盖 Left/Center/Right/Near/Far；正常光+略变光；Approach A/B/C
- 实际：2026-09-10 录了 20 条成功抓放（约 15s×20，9000 帧），**尚未做位置/光照覆盖网格**
- 差距：数量 20/100；多样性未按课表铺开；分析 notebook 未建
- 下次实践：E01 训完后 `num_episodes=30` resume 到 50，再 `=50` 到 100

### W3 ACT

- 课表：E01(20) → E02(50) → E03(100)，先这一条不要并行 DP/VLA
- 实际：E01 01:21 启动，20K 遇 P005 中断后 resume；03:03 约 **30K/100K**，loss≈0.098
- 差距：未到 100K；E02/E03 未开始

### W4–W12

尚未实践。

## 偏离 / 拦截

| 日期 | 事项 | 处理 |
|------|------|------|
| 2026-09-10 | 训练读盘期间不可 resume 同一数据集 | 已写入课表「现在立刻」 |

## 每周节奏（对照用）

课表：一/二工程，三/四算法，五记实验，六日大实验。  
2026-09-10（周四）：符合「算法：训练」。
