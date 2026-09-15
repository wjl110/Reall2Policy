# ACT vs Diffusion Policy（同一 Dataset）

Dataset：`so101_pick_place_20260910_011033` 100 ep / 65100 帧
日期：ACT 列为 E03（2026-09-12 评测）；DP 100K @2026-09-15 08:34

| | ACT E03 | Diffusion |
|---|---:|---:|
| IID Success | 37/90 | |
| OOD Success | Pos 0/90 | |
| Training Time | 约 2.5–3 h（bf16 100K） | 约 36.7 h（13日 19:50 → 15日 08:34） |
| Inference Latency | | |
| Grasp Failure | 见 `eval_w56.md` | |
| Placement Failure | 见 `eval_w56.md` | |

下一步：`pretrained_model_ema` 真机 IID。100K loss 无日志，不以 loss 判胜负。
