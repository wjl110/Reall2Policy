# Experiments

填真实数字。W5–6 齐。IID 37/90；Pos/Obj 0；Light=Bg 1；Cam 19/90。

| Exp | 周 | Policy | Episodes | Steps | Camera | Loss | IID Success | 输出 | 状态 |
|---|---|---|---:|---:|---|---:|---:|---|---|
| E01 | W3 | ACT | 20 | 100000 | 1 | 0.051 @100K | 姿态对齐后成功（未计次） | `outputs/train/act_so101_pick_place` | **完成** |
| E02 | W3 | ACT | 50 | 100000 | 1 | 0.065 @100K | 一轮 OK；第二轮折叠卡死 | `outputs/train/act_so101_e02` | **完成**（真机部分成功） |
| E03 | W3 | ACT | 100 | 100000 | 1 | 0.168 @100K | 连续抓取 OK（单次，未见折叠） | `outputs/train/act_so101_e03` | **完成（bf16）** |
| E04 | W4 | ACT 真机 | 100 | 100000 | 1 | 0.168 @E03 | E03 连续抓取 OK | `assets/demo.mp4` | **完成** |
| E05 | W5–6 | ACT eval/OOD | 100 | 100000 | 1 | 0.168 @E03 | 37 / 0 / 0 / 1 / 19 | `results/eval_w56.md` | **完成** |
| E06 | W7 | DAgger→ACT-v2 | 14 | 20000 | 1 | | | `act_so101_v2/020000` | **训练中**（监控断） |
| E07 | W8 | Diffusion | 同 E03 数据 | 100000 | 1 | | | `outputs/train/dp_so101_v1` | 未开始 |
| E08 | W9–10 | SmolVLA | | | 1 | | | `outputs/train/smolvla_so101_v1` | 未开始 |
