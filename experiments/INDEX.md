# Experiments

填真实数字。E02 重训 ~58K/100K，ckpt 20K/40K。

| Exp | 周 | Policy | Episodes | Steps | Camera | Loss | IID Success | 输出 | 状态 |
|---|---|---|---:|---:|---|---:|---:|---|---|
| E01 | W3 | ACT | 20 | 100000 | 1 | 0.051 @100K | 姿态对齐后成功（未计次） | `outputs/train/act_so101_pick_place` | **完成** |
| E02 | W3 | ACT | 50 | 100000 | 1 | 0.086 @58K | | `outputs/train/act_so101_e02` | **进行中 ~58K/100K** |
| E03 | W3 | ACT | 100 | 100000 | 1 | | | `outputs/train/act_so101_e03` | 未开始 |
| E04 | W4 | ACT 真机 | 20 | 100000 | 1 | — | 对齐后 OK；折叠失败 | rollout + README GIF | **进行中**（缺 demo.mp4） |
| E05 | W5–6 | ACT eval/OOD | | | 1 | — | | `results/eval_w56.md` | 未开始 |
| E06 | W7 | ACT-v2 | | 100000 | 1 | | | `outputs/train/act_so101_v2` | 未开始 |
| E07 | W8 | Diffusion | 同 E03 数据 | 100000 | 1 | | | `outputs/train/dp_so101_v1` | 未开始 |
| E08 | W9–10 | SmolVLA | | | 1 | | | `outputs/train/smolvla_so101_v1` | 未开始 |
