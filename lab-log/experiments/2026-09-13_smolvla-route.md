# W9 路线：smolvla_base 微调 vs 从零

- 状态：建议已确认，**现在不执行**（W7 在训 ACT-v3）
- 时间：2026-09-13 14:04
- 课表：W9–10 预案（未到该周）
- 对照：[SmolVLA 文档](https://huggingface.co/docs/lerobot/smolvla)、[官方博客](https://huggingface.co/blog/smolvla)

## 做了什么

用户问两条路哪个好。对照官方配方和本机课表命令、数据量、8GB 显存、W9 语言指令目标。

## 两条官方配方（不是课表自己发明的）

| | 微调 `smolvla_base` | 从零 `--policy.type=smolvla` |
|--|---------------------|------------------------------|
| 开关 | `--policy.path=lerobot/smolvla_base` | 只有 `--policy.type=smolvla` |
| 初始化 | 完整 VLA（VLM + action expert） | 架构；本机默认 `load_vlm_weights=False` |
| 官方步数 | **20K**（博客写 10% 预算） | **200K** |
| 官方数据建议 | 约 50 ep 再微调 | 社区预训那种规模 |
| 课表现在 | 没有这条 | 从零 + **20K**（预算用错了） |

本机课表 `docs/COURSE.md` W9 和 `configs/smolvla.yaml`：`--policy.type=smolvla --steps=20000 --batch_size=4`。这是「从零的开关」配「微调的步数」。

## 为什么选微调

1. SmolVLA 官方定位就是 **base，必须在自己数据上微调**。
2. 本机只有 100–111 ep、单 `front`。VLA 从零学「看图 + 语言 + 6 轴」不够。ACT-v2 已经用小数据从零证过一次。
3. W9 要语言指令。base 的 VLM 已经会跟指令；从零还要在百条里把语言和动作一起学出来。
4. 8GB 只能 batch=4。从零 200K 墙钟太长；课表 20K 从零等于没训够。
5. 微调仍用**本机**数据，不是混官方 `svla_so101_pickplace`。

## 从零什么时候才有意义

消融「预训有没有用」、换了完全对不上的本体、或有社区级数据。本课表三条都不成立。

## 决定

- **W9 走官方微调。** 2026-09-13 14:13 已改 `docs/COURSE.md` / `configs/smolvla.yaml`：`--policy.path=lerobot/smolvla_base`，数据 `local/so101_lang`，batch 4，20K，不上 Hub。语言集尚未采集。
- 单相机若报错，课表已写可加 `--policy.empty_cameras=1`。
- **现在不开。** 等 ACT-v3 100K。不并行 VLA。

## 效果

只定路线，未下载权重，未开训。
