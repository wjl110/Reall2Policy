# 当前状态

更新：2026-09-10 03:22

## 课表

**W3 E01 进行中 + W2 数据 20/100。** 详见 [course.md](course.md)。图表：[charts.md](charts.md)。  
本周该做：让 ACT 接着跑。本周不要：补采同一数据集、开 Diffusion/SmolVLA、做 W11。

## 正在跑

ACT 训练 **resume 中**（终端 `activate.cmd`）。

- 约 **step 40K** / 100K，loss≈0.082，l1≈0.078，~9.7 step/s，显存 2.10 GB
- 已写入 **`checkpoints/040000`**（存盘成功）
- 输出：`outputs/train/act_so101_pick_place`
- **不要停，不要往这份数据里 resume 录制**

## 最新可用数据

| 项 | 值 |
|----|-----|
| 数据集 | `data/local/so101_pick_place_20260910_011033` |
| 规模 | 20 episodes / 9000 frames（课表目标 100） |
| 权重 | `checkpoints/020000`、`040000` |
| 课表完成度 | 约 23% |
| 飞轮 | 卡在加采（训练占用同一 root） |

## 阻塞 / 未完成

- E01 未到 100K。
- Week 2：20/100，且未做位置/光照网格。
- GitHub 杂数据删除随本版推送。
- 实机 rollout 未做。

## 下一步（按课表）

1. 让 E01 跑完 100K。
2. 训练结束后补采 +30→50，再 +50→100。
3. 再训 E02/E03；然后 W4 拔 Leader 做 rollout。
