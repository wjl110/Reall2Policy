# Experiments

填真实数字。W5–6 齐。E03 IID 37/90 Pos 0/90。v3 IID 8/90 Pos 13/90。Obj 0；Light=Bg 1；Cam 19/90。

| Exp | 周 | Policy | Episodes | Steps | Camera | Loss | IID Success | 输出 | 状态 |
|---|---|---|---:|---:|---|---:|---:|---|---|
| E01 | W3 | ACT | 20 | 100000 | 1 | 0.051 @100K | 姿态对齐后成功（未计次） | `outputs/train/act_so101_pick_place` | **完成** |
| E02 | W3 | ACT | 50 | 100000 | 1 | 0.065 @100K | 一轮 OK；第二轮折叠卡死 | `outputs/train/act_so101_e02` | **完成**（真机部分成功） |
| E03 | W3 | ACT | 100 | 100000 | 1 | 0.168 @100K | 连续抓取 OK（单次，未见折叠） | `outputs/train/act_so101_e03` | **完成（bf16）** |
| E04 | W4 | ACT 真机 | 100 | 100000 | 1 | 0.168 @E03 | E03 连续抓取 OK | `assets/demo.mp4` | **完成** |
| E05 | W5–6 | ACT eval/OOD | 100 | 100000 | 1 | 0.168 @E03 | 37 / 0 / 0 / 1 / 19 | `results/eval_w56.md` | **完成** |
| E06 | W7 | DAgger→ACT-v2 | 14 | 100000 | 1 | | IID 0/15；Pos 0/15 | `act_so101_v2/100000` | **弱于 E03** |
| E06b | W7 | 100+dagger3→v3 | 111 | 100000 | 1 | 无日志 | IID 8/90；Pos 13/90 | `act_so101_v3/100000` | **IID 弱于 E03；Pos 强于 E03** |
| E07 | W8 | Diffusion | 100 | 100000 | 1 | 0.021 @14K | 待 IID | `dp_so101_v1/100000` | **训练完成，待复测** |
| E08 | W9–10 | SmolVLA | | | 1 | | | `outputs/train/smolvla_so101_v1` | 未开始 |
