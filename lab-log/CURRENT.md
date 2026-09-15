# 当前状态

更新：2026-09-15 08:34

## 课表

**W8 进行中。** Diffusion **100K 已齐**。日常演示仍用 E03。不要开 VLA。下一步真机对照。

## 正在跑

无训练。`dp_so101_v1` 已结束。ckpt **100000 @08:34:20**（含 `pretrained_model_ema`）。

## 最新可用数据

| 项 | 值 |
|----|-----|
| 日常 / 夹下 | **E03** `act_so101_e03/100000` · IID 37/90 |
| 找物 | v3 · Pos 13/90 |
| W8 DP | `dp_so101_v1/checkpoints/100000/pretrained_model_ema` |

## 阻塞 / 未完成

- DP 尚未真机比。100K loss 无日志，不编造。
- W9 现在不开。

## 下一步（按课表）

先 `start.cmd`，摆到录制起始姿态，用 EMA 做 IID。填 `results/act_vs_dp.md`。
