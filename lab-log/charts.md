# 学习进程与曲线

数据：[`metrics.json`](metrics.json)（2026-09-13 04:43）。规范：Skill 内 `charts-spec.md`。

## 学习进程（12 周完成度 %）

整体约 **66%**（各周算术平均）。

```mermaid
xychart-beta
    title 12周课表完成度
    x-axis ["W0","W1","W2","W3","W4","W5-6","W7","W8","W9-10","W11","W12"]
    y-axis "完成度 %" 0 --> 100
    bar [100, 100, 100, 100, 100, 100, 85, 0, 0, 0, 25]
```

W5–6 齐。Cam 19/90。W7 先 DAgger 找物。

## 项目收益（计划 vs 已兑现，0–10）

```mermaid
xychart-beta
    title 各周作品集收益
    x-axis ["W0","W1","W2","W3","W4","W5-6","W7","W8","W9-10","W11","W12"]
    y-axis "分" 0 --> 10
    bar [2, 4, 6, 7, 9, 8, 8, 9, 9, 6, 10]
    bar [2, 4, 6, 7, 9, 8, 6, 0, 0, 0, 4]
```

第一组 = 课表计划分；第二组 = 已兑现。IID 数字已齐。

## 学习曲线（ACT E01）

20K 前 loss 约 7.0→0.13，未画入。

```mermaid
xychart-beta
    title ACT E01 loss 与 l1_loss
    x-axis [20, 22, 24, 30, 33, 35, 37, 39, 40, 100]
    y-axis "loss" 0.04 --> 0.14
    line [0.127, 0.121, 0.111, 0.098, 0.092, 0.088, 0.085, 0.083, 0.082, 0.051]
    line [0.111, 0.107, 0.101, 0.090, 0.086, 0.084, 0.081, 0.080, 0.078, 0.051]
```

最终权重：`act_so101_pick_place/checkpoints/100000`。

## 学习曲线（ACT E02 重训）

20K 前骤降未画入。100K 完成，loss 0.065 / l1 0.064。

```mermaid
xychart-beta
    title ACT E02 loss 与 l1_loss
    x-axis [20, 40, 50, 58, 94, 100]
    y-axis "loss" 0.05 --> 0.22
    line [0.206, 0.120, 0.096, 0.086, 0.066, 0.065]
    line [0.174, 0.114, 0.094, 0.084, 0.066, 0.064]
```

最终权重：`act_so101_e02/checkpoints/100000`。

## 学习曲线（ACT E03 bf16，100K 完成）

200→4K 骤降（7.026→0.665）不与本图同轴。24K–92K 终端回滚丢失。最终 loss 0.168 / l1 0.097 / kld 0.007。预测曾是 0.07–0.09。

```mermaid
xychart-beta
    title ACT E03 loss 与 l1_loss
    x-axis [20, 24, 92, 94, 96, 97, 99, 100]
    y-axis "loss" 0.09 --> 0.25
    line [0.243, 0.233, 0.171, 0.171, 0.170, 0.164, 0.167, 0.168]
    line [0.212, 0.202, 0.100, 0.099, 0.099, 0.094, 0.096, 0.097]
```

最终权重：`act_so101_e03/checkpoints/100000`。

## 学习曲线（ACT-v2）

02:32 开训。早期 200–800：6.967→2.413。**20/40/60/80K ckpt 已落**。这些点的 loss 被进度条覆盖，不画虚点。

## 数据回收飞轮

```mermaid
flowchart LR
    A["采集 100/100 done"] --> B["训练 E03 done"]
    B --> C["真机评估 E03 done"]
    C --> D["失败归类 Position done"]
    D --> E["加采 dagger2 14ep done"]
    E --> F["ACT-v2 in_progress"]
```

下一环：ACT-v2 仍在跑，`080000` 已齐。实时监控 `lab-log/train-live.html`。
