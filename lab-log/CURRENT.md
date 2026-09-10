# 当前状态

更新：2026-09-10 23:17

## 课表

**W2 本批完成：50/100。下一步 W3 E02 训练（50 ep）。**  
不要并行 DP/VLA；不要另开数据集目录。

## 正在跑

无。录制已正常结束（25 集本轮，29.98 Hz）。

## 最新可用数据

| 项 | 值 |
|----|-----|
| 数据集 | `data/local/so101_pick_place_20260910_011033` |
| 规模 | **50 episodes / 27000 frames** / 30 fps |
| 权重 | E01 `checkpoints/100000`（20 ep 上训的） |
| 真机 | 对齐后抓放成功（P010） |

## 阻塞 / 未完成

- 总目标仍缺 50 集（E03 用）。
- W4 Demo 未录。

## 下一步（按课表）

训 E02（新输出目录，勿覆盖 E01）：

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=act --output_dir=outputs/train/act_so101_e02 --job_name=act_so101_e02 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=8 --steps=100000
```
