---
name: reall2policy-lab-log
description: >-
  Reall2Policy / SO-ARM101 实验台账、课表学习跟踪与图表。每次加载或打开本项目、开始新对话、做校准/遥操/录制/回放/训练/评估、
  对照 docs/COURSE.md 学习实践、绘制学习进程/项目收益/学习曲线/数据回收图、出现报错或踩坑时必须先读并执行本 Skill：
  记录做了什么、实验数据、效果、重要日志、节点信息、课表周次完成度，并更新图表。
  触发词：实验、训练、录制、校准、踩坑、日志、数据集、checkpoint、COM口、启动项目、课表、COURSE、
  学习、实践、Week、E01、学习曲线、收益图、数据回收、flywheel、图表。
---

# Reall2Policy 实验台账 + 课表跟踪 + 图表

项目实验、踩坑、12 周学习实践与可视化的唯一记录系统。

- 台账根目录：`lab-log/`
- 课表原文（只给用户抄命令）：`docs/COURSE.md`
- 学习进度（Agent 维护）：`lab-log/course.md`
- 图表数据：`lab-log/metrics.json` → `lab-log/charts.md`（规范见 [charts-spec.md](charts-spec.md)）

**每次新对话的第一条动作必须是读本 Skill，并执行「会话启动」。不得跳过。**

## 会话启动（每次加载项目 / 新对话）

按顺序做，再回答用户：

1. 读 `lab-log/CURRENT.md`、`lab-log/INDEX.md`、`lab-log/course.md`。
2. 读 `docs/COURSE.md` 顶部状态表，与磁盘事实核对（数据 episodes、训练 step、eval 文件）。
3. 扫终端：是否有 `lerobot-train` / `lerobot-record` / `lerobot-calibrate` / `lerobot-eval` / `lerobot-rollout` 在跑；记下 step、loss、报错。
4. 对照 `data/local/*/meta/info.json` 与 `outputs/train/**/checkpoints/`，INDEX 没有的立刻补记。
5. 对照 `lab-log/metrics.json`：step/loss/episodes 有变则先改 json，再重画 `lab-log/charts.md`（学习进程、项目收益、学习曲线、数据回收）。数字没变则不重画。
6. 在 `lab-log/sessions/` 新建或追加当天会话文件。
7. 用 **5–10 行中文** 汇报：课表第几周、本周该做/禁止做、在跑任务、最新数据/权重、曲线最新点、飞轮卡在哪一环、未关闭的坑、建议下一步（必须来自课表，禁止跳周）。然后才处理用户请求。

## 学习实践跟踪（对照课表）

课表是学习计划；`lab-log/course.md` 是「实际练了没有」。每次启动和每次实践后都要同步。

| 周 | 课表目标 | 怎样算练过 |
|----|----------|------------|
| W0 | 环境 | `verify.cmd` 通过 |
| W1 | 遥操 | 校准文件存在 + teleop 跑通过 |
| W2 | 100 ep | `info.json` 的 `total_episodes`（现 20，目标 100） |
| W3 | ACT E01/E02/E03 | 对应 `outputs/train/act_so101_*` 的数字 checkpoint |
| W4 | 拔 Leader | 真机 rollout + `assets/demo.mp4` |
| W5–6 | Eval/OOD | `results/eval_w56.md` 填了次数 |
| W7 | Data flywheel | 加采 hard cases + ACT-v2 |
| W8 | ACT vs DP | `results/act_vs_dp.md` |
| W9–10 | SmolVLA | 语言指令数据 + smolvla 输出 |
| W11 | World Model | 到该周再写，**提前做 = 偏离** |
| W12 | 作品集 | GitHub 远程 + Demo 结构 |

同步规则：

- **磁盘变了**（episodes、step、新 ckpt、新结果文件）→ 更新 `lab-log/course.md` **和** `docs/COURSE.md` 顶部状态表，并刷新图表。
- **用户完成了某周一步** → 该周标完成/进行中，记下日期、命令、效果；`experiments/INDEX.md` 同步 E01–E08。
- **用户想跳周或并行 DP/VLA** → 先对照课表拦住，写进 course.md「偏离」，再问是否仍要做。
- 会话汇报必须带一句：**本周实践 vs 课表**。

课表硬约束（实践时不得违反，除非用户书面坚持）：

- 训练占用 GPU 时，**不要**同一窗口录数据，**不要** `resume` 正在被训练读的数据集。
- W3 先做完当前这条 ACT，不要并行 Diffusion / SmolVLA。
- 任务只做一件：`Pick up the object and place it down.`（W9 语言指令除外）。
- 给用户的下一步命令优先从 `docs/COURSE.md` 复制，不要另编一套。

## 何时立刻落盘（不要等对话结束）

下列任一发生，**先写文件，再回复用户**：

| 事件 | 写到 |
|------|------|
| 校准 / 遥操 / 录制 / 回放 / 训练 / 评估 / rollout 开始或结束 | `experiments/` + INDEX、CURRENT、course.md |
| 课表某周进度变化、完成一项练习、跳周/偏离 | `lab-log/course.md` + `docs/COURSE.md` 状态表 + `experiments/INDEX.md` |
| 报错、奇怪现象、绕过方法 | `pitfalls/INDEX.md`（已有则追加「再现」） |
| 串口、摄像头、GPU、环境版本变化 | `nodes/hardware.md` |
| 重要日志片段、checkpoint、数据集路径 | 对应实验条目的「日志 / 节点」 |
| 用户说「完成了 / 失败了 / 效果如何」 | 补全效果与结论，并勾课表 |
| checkpoint / episodes / eval 数字变化 | `metrics.json` + `charts.md` 四张图 |

禁止只在聊天里总结、不写 `lab-log/`。

## 四张必更图

有新数字时四张一起更新，缺数据的图省略该 series，不要画全 0 占位。细则见 [charts-spec.md](charts-spec.md)。

| 图 | 文件 | 含义 |
|----|------|------|
| 学习进程 | charts.md 第一节 | W0–W12 完成度 % |
| 项目收益 | charts.md 第二节 | 各周计划分 vs 已兑现分（作品集价值） |
| 学习曲线 | charts.md 第三节 | ACT/其他 job 的 loss、l1 vs step |
| 数据回收 | charts.md 第四节 | 采集→训练→评估→失败归类→加采 飞轮 |

对话里用 Cursor Canvas 展示同一份 `metrics.json` 数字，与 `charts.md` 保持一致。

## 记录必须包含

每条实验至少有：做了什么、实验数据、效果怎么样、重要日志、节点信息。

学习实践额外要有：**对应课表哪一周 / 哪条 Exp**、计划 vs 实际、差距（例如 20/100 ep）。

踩坑至少有：症状、根因、解法、以后怎么避免。

## 目录与命名

```
lab-log/
  INDEX.md                 # 总览（始终先读）
  CURRENT.md               # 当前状态（始终先读、始终更新）
  course.md                # 课表学习实践（始终先读、对照 COURSE.md）
  metrics.json             # 图表唯一数据源
  charts.md                # 学习进程 / 收益 / 曲线 / 飞轮
  sessions/YYYY-MM-DD.md
  experiments/YYYY-MM-DD_<短名>.md
  pitfalls/INDEX.md
  nodes/hardware.md
docs/COURSE.md             # 用户抄命令的课表（Agent 只改顶部状态表）
experiments/INDEX.md       # E01–E08 数字
```

- 实验短名用英文连字符：`act-train`、`pick-place-20`。
- 进行中的实验在 INDEX 标 `进行中`；结束改为 `成功` / `失败` / `中断`。
- 同一次训练的续跑写在**同一实验文件**，追加「节点」。

## 扫描约定

- 数据集：`data/local/<name>/meta/info.json` → `total_episodes`、`total_frames`、`fps`、`robot_type`。
- 空目录（episodes=0）记为「未完成/冲突改名残留」，不要当正式数据。
- 训练：`outputs/train/<job>/checkpoints/<step>/`；Windows 上 `last` 可能不存在，以数字目录为准。
- 校准：`calibration/robots/so_follower/`、`calibration/teleoperators/so_leader/`。
- 环境：`logs/verification.json`。
- 课表进度：episodes 看 info.json；训练 step 看终端 `step:` 或最大 checkpoint 目录名。
- 学习曲线：从终端 `step:` / `loss:` / `l1_loss:` 采样写入 `metrics.json`。

## 硬规则（本机）

- 录制/训练默认 `--dataset.push_to_hub=false`、`--policy.push_to_hub=false`、`--wandb.enable=false`。
- 凡带相机的 `lerobot-record` / `lerobot-teleoperate` / `lerobot-rollout`，默认加 `--display_data=true`（Rerun 实时画面）。给用户抄的命令不得漏这一项。`lerobot-replay` 无此开关。
- 本地数据集训练加 `--dataset.video_backend=pyav`，并写明 `--dataset.root=`（时间戳目录）。
- 串口：Leader=`COM3` / `so101_leader`；Follower=`COM4` / `so101_follower`。变化则更新 `nodes/hardware.md`。
- 不把 token、`.env`、密钥写入 lab-log。

完整模板见 [templates.md](templates.md)。
