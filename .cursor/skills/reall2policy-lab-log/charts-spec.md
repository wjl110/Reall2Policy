# 图表规范

数据源只有 `lab-log/metrics.json`。仓库内图：`lab-log/charts.md`。对话看板：Cursor Canvas（数字必须与 json 一致）。

更新前先改 json，再改 mermaid / canvas。没有新数字就不要重画。

## 1. 学习进程

- 横轴：W0–W12；纵轴：完成度 0–100%。
- 完成度算法：该周「怎样算练过」的比例（见 SKILL）。W3 = E01 step/100K（E02/E03 未开始不均摊进分母以外的虚高）。整体完成度 = 12 周算术平均。
- 标题：`12 周课表完成度（%）`。来源：`docs/COURSE.md` + 磁盘证据。

## 2. 项目收益图

- 每周对作品集的**计划分**（课表设计，0–10）vs **已兑现分**（实际产物）。
- 已兑现须有证据：无真机成功率就不要把 W4 画满。
- 标题：`各周作品集收益：计划 vs 已兑现（0–10）`。

默认计划分：W0=2, W1=4, W2=6, W3=7, W4=9, W5–6=8, W7=8, W8=9, W9–10=9, W11=6, W12=10。

## 3. 学习曲线

- 从终端 `ot_train.py` 的 `step:` / `loss:` / `l1_loss:` 追加点；约每 2–5K step 留一个，checkpoint 必留。
- 不要把 step 0 的 loss≈7 和 20K 以后画在同一纵轴上（会压扁曲线）。早期骤降写在 caption，图从首个稳定段（本项目 20K）起，`beginAtZero=false`。
- 标题：`ACT E01 训练曲线：loss / l1_loss vs step`。单位：step（千）、无量纲 loss。
- 新 policy（E02/DP/VLA）另开 series，不要覆盖 E01。

## 4. 数据回收（flywheel）

环：采集 → 训练 → 真机评估 → 失败归类 → 加采 hard cases → 再训练。

- 节点状态：`done` / `in_progress` / `blocked` / `pending`。
- 数量：episodes 当前/目标、hard cases 条数、回收轮次。
- 标题：`数据回收飞轮（当前轮次与阻塞）`。
- 训练读盘时采集节点标 `blocked`。

## 会话汇报

图表更新后，汇报里加一行：曲线最新点、课表完成度、飞轮卡在哪一环。
