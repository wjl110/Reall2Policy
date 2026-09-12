# 课表学习实践跟踪

课表原文（抄命令）：[`docs/COURSE.md`](../docs/COURSE.md)  
实验数字：[`experiments/INDEX.md`](../experiments/INDEX.md)  
更新：2026-09-13 04:45

## 当前焦点

**W7：ACT-v2 正常在跑**（`080000` 已落）。实时监控已开。

本周实践 vs 课表：加采完成，训练过 80K，未到 100K。

## 总进度

| 周 | 课表目标 | 实践状态 | 证据 | 差距 |
|----|----------|----------|------|------|
| W0 环境 | verify | **完成** | `logs/verification.json` | 无 |
| W1 遥操 | 校准 + teleop | **完成** | `calibration/` COM3/COM4 | 无 |
| W2 数据 | 100 episodes | **完成 100/100** | `so101_pick_place_20260910_011033` 65100 帧 | 无 |
| W3 ACT | E01/E02/E03 各 100K | **完成** | E03 `100000` loss 0.168 | 进入 W4 rollout |
| W4 拔 Leader | 真机 rollout + Demo | **完成** | `assets/demo.mp4` 约 105MB | 进库前需压缩 |
| W5–6 Eval/OOD | 填评测表 | **完成** | Cam 19/90；Pos/Obj 0 | 无 |
| W7 Flywheel | hard cases + ACT-v2 | **进行中** | v2 `080000` | 未到 100K |
| W8 ACT vs DP | 同数据对比 | 未开始 | 模板 `results/act_vs_dp.md` | 禁止现在并行 |
| W9–10 SmolVLA | 语言指令 | 未开始 | — | 禁止现在并行 |
| W11 World Model | 预测实验 | 未开始 | — | **不到该周不要做** |
| W12 作品集 | GitHub + Demo | 进行中 | https://github.com/wjl110/Reall2Policy | README 四格 Demo + 评测聚类 + 作者信息 |

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
- 实际：2026-09-10 先 20 再 50；2026-09-12 **resume 完成 100 ep / 65100 帧**（本批 32×20s + 18×35s）
- 差距：无（条数达标；位置网格未逐条核）
- 下次实践：已完成

### W3 ACT

- 课表：E01(20) → E02(50) → E03(100)
- 实际：E01 **100K** loss≈0.051。E02 **100K** loss≈0.065。E03 bf16 **04:38 100K** loss 0.168（P014 后从 20K resume）
- 差距：无（训练目标已齐）

### W4 拔 Leader

- 课表：rollout + `assets/demo.mp4`
- 实际：2026-09-10 E01 姿态对齐后 OK。2026-09-11 E02：第一轮 OK，第二轮 P013。2026-09-12 E03：连续抓取 OK，未见折叠；`assets/demo.mp4` 已齐
- 差距：无（进库前需压到 100MB 以下）

### W5–6 Eval/OOD

- 课表：6 种条件各 30–50 次，填 `results/eval_w56.md`
- 实际：IID 37/90；Pos 0；Obj 0；Light=Bg 1/90；Cam 19/90
- 差距：无（表已齐）

### W7 Flywheel

- 课表：W6 最差条件加采 + ACT-v2
- 计划：2026-09-12 约定 W5–6 完成后用官方 `--strategy.type=dagger --strategy.record_autonomous=true`（整段保存，纠正打 `intervention`）
- 约束：新开 `local/rollout_so101_dagger`，不 resume 现有 100 ep；插回 Leader
- 实际：第一趟 0 ep（P018）。dagger2 **14 ep / 37494 帧**。02:32 开 ACT-v2；20/40/60K 已落；04:40 **`080000`**
- 差距：训练未到 100K

### W12 作品集

- 课表：GitHub + Demo 结构
- 实际：2026-09-13 README Demo 四格；同日补评测聚类（`eval_w56.md`）与作者信息
- 差距：W8–W11 未做；作品集结构未齐

### W8–W11

W8 起尚未按评测表实践。

## 偏离 / 拦截

| 日期 | 事项 | 处理 |
|------|------|------|
| 2026-09-10 | 训练读盘期间不可 resume 同一数据集 | 已解除（E01 结束） |
| 2026-09-10 | W4 rollout 在 W2 补满前做了 | 允许：E01 权重已可用；下一步仍回 W2 补采，不跳去 DP/VLA |
| 2026-09-11 | 未满 100 ep 就想训 E03 | 拦住：先 +50 再 E03 |

## 每周节奏（对照用）

课表：一/二工程，三/四算法，五记实验，六日大实验。  
2026-09-10（周四）：W3 结束 + W4 初验；晚间进入 W2 补采。
