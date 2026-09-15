# 官方可复用 / 提效（对照本机）

- 状态：结论，不改正在跑的 v3
- 时间：2026-09-13 14:21
- 课表：W7
- 对照：[Compute HW Guide](https://huggingface.co/docs/lerobot/main/hardware_guide)、[ACT](https://huggingface.co/docs/lerobot/en/act)、[SmolVLA](https://huggingface.co/docs/lerobot/smolvla)、[Cameras](https://huggingface.co/docs/lerobot/cameras)

## 慢在哪（不是缺一个魔法开关）

官方 ACT 就是从零、约 50–100 ep、batch 8、数小时。本机已按这条走：bf16、pyav、DAgger、100K。

真正耗时是**流程重复**，不是单次 step 比官方慢一个数量级：

- 已从零满跑 5 次 100K（E01/E02/E03/v2/v3）
- 本机条均约 30s / 890 帧；官方示例 pickplace 约 8–10s
- W5–6 计次 450；官方没有要求这么多
- v3：98723 帧 / batch 8 ≈ 1.23 万 step/epoch。官方写模仿学习常 **5–10 个 epoch**，100K ≈ 8 epoch，预算本身合理

单卡 8GB、~10 step/s、100K ≈ 2.5–3h，对照官方 4090 上「50 ep / 5 epoch / 30–60min」并不离谱。

## 官方能复用

| 项 | 对本机 | 何时 |
|----|--------|------|
| `lerobot/smolvla_base` 微调 20K | 已写入 W9 课表 | W9，现在不开 |
| DAgger / HITL | 已在用 | 飞轮继续 |
| ACT 从零 + ImageNet backbone | 已在用 | — |
| `--dataset.image_transforms.enable=true` | 配置里有，**当前是 false** | 下一轮训（光/位 OOD） |
| 5–10 epoch 收束，不必每次 100K 从零 | 下一轮从 v3/E03 接着微调 | v3 评完以后 |
| 条短一点，放下就停 | 少闲置帧 | 下次采集 |
| `empty_cameras` / `freeze_vision_encoder` | W9 微调 | W9 |
| 异步推理 / RTC | 只加快 rollout 手感 | W9 部署 |

## 官方不能当提效

- 混 `svla_so101_pickplace` 进 ACT（相机/校准不对）
- 本机单 `front` 没有可即插的官方 ACT 权重
- π₀ / π₀.₅：官方 24–40GB，8GB 不够
- HF Jobs：本机有 GPU，且默认不上 Hub（P002）
- 多卡 `accelerate`：只有一张 5060 Ti

## 决定

- **现在：** 不改 v3、不下载、不开第二路。
- **W9：** 按已改课表微调 base，20K。
- **下一轮 ACT：** 不要再从零 100K；`--policy.path=` 现有 ckpt + 变换开着 + 更短条。
