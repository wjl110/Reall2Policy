# Experiments

填真实数字。E01 进行中。

| Exp | 周 | Policy | Episodes | Steps | Camera | Loss | IID Success | 输出 | 状态 |
|---|---|---|---:|---:|---|---:|---:|---|---|
| E01 | W3 | ACT | 20 | 100000 | 1 | ~0.098 @30K | | `outputs/train/act_so101_pick_place` | 进行中 ~30K/100K |
| E02 | W3 | ACT | 50 | 100000 | 1 | | | `outputs/train/act_so101_e02` | 未开始 |
| E03 | W3 | ACT | 100 | 100000 | 1 | | | `outputs/train/act_so101_e03` | 未开始 |
| E04 | W4 | ACT 真机 | | | 1 | — | | rollout Demo | 未开始 |
| E05 | W5–6 | ACT eval/OOD | | | 1 | — | | `results/eval_w56.md` | 未开始 |
| E06 | W7 | ACT-v2 | | 100000 | 1 | | | `outputs/train/act_so101_v2` | 未开始 |
| E07 | W8 | Diffusion | 同 E03 数据 | 100000 | 1 | | | `outputs/train/dp_so101_v1` | 未开始 |
| E08 | W9–10 | SmolVLA | | | 1 | | | `outputs/train/smolvla_so101_v1` | 未开始 |
