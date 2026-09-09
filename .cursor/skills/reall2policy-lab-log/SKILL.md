---
name: reall2policy-lab-log
description: >-
  Reall2Policy / SO-ARM101 实验台账。每次加载或打开本项目、开始新对话、做校准/遥操/录制/回放/训练/评估、
  出现报错或踩坑时必须先读并执行本 Skill：记录做了什么、实验数据、效果、重要日志与节点信息。
  触发词：实验、训练、录制、校准、踩坑、日志、数据集、checkpoint、COM口、启动项目。
---

# Reall2Policy 实验台账

项目实验与踩坑的唯一记录系统。根目录：`lab-log/`。

**每次新对话的第一条动作必须是读本 Skill，并执行「会话启动」。不得跳过。**

## 会话启动（每次加载项目 / 新对话）

按顺序做，再回答用户：

1. 读 `lab-log/CURRENT.md` 和 `lab-log/INDEX.md`。
2. 扫终端：是否有 `lerobot-train` / `lerobot-record` / `lerobot-calibrate` / `lerobot-eval` 在跑；记下 step、loss、报错。
3. 对照 `data/local/*/meta/info.json` 与 `outputs/train/**/checkpoints/`，发现 INDEX 里没有的新数据立刻补记。
4. 在 `lab-log/sessions/` 新建或追加当天会话文件（见模板）。
5. 用 **5–8 行中文** 向用户汇报：当前节点、在跑的任务、最新数据集/权重、未关闭的坑、建议下一步。然后才处理用户请求。

## 何时立刻落盘（不要等对话结束）

下列任一发生，**先写文件，再回复用户**：

| 事件 | 写到 |
|------|------|
| 校准 / 遥操 / 录制 / 回放 / 训练 / 评估 开始或结束 | `experiments/` + 更新 INDEX、CURRENT |
| 报错、奇怪现象、绕过方法 | `pitfalls/INDEX.md`（已有则追加「再现」） |
| 串口、摄像头、GPU、环境版本变化 | `nodes/hardware.md` |
| 重要日志片段、checkpoint、数据集路径 | 对应实验条目的「日志 / 节点」 |
| 用户说「完成了 / 失败了 / 效果如何」 | 补全效果与结论 |

禁止只在聊天里总结、不写 `lab-log/`。

## 记录必须包含

每条实验至少有：

- **做了什么**：命令（可复现）、目的
- **实验数据**：`repo_id`、`--dataset.root`、episodes、frames、fps、相机、任务描述
- **效果怎么样**：成功 / 失败 / 进行中；loss、速度、显存、实机表现
- **重要日志**：关键 INFO/ERROR 原文（精简，不要整段配置 dump）
- **节点信息**：COM 口、robot.id、GPU、checkpoint 步数、时间

踩坑至少有：症状、根因、解法、以后怎么避免。

## 目录与命名

```
lab-log/
  INDEX.md                 # 总览（始终先读）
  CURRENT.md               # 当前状态（始终先读、始终更新）
  sessions/YYYY-MM-DD.md   # 按日会话
  experiments/YYYY-MM-DD_<短名>.md
  pitfalls/INDEX.md
  nodes/hardware.md
```

- 实验短名用英文连字符：`act-train`、`pick-place-20`。
- 进行中的实验在 INDEX 标 `进行中`；结束改为 `成功` / `失败` / `中断`。
- 同一次训练的续跑写在**同一实验文件**，追加「节点」，不要新开无关文件。

## 扫描约定

- 数据集：`data/local/<name>/meta/info.json` → `total_episodes`、`total_frames`、`fps`、`robot_type`。
- 空目录（episodes=0）记为「未完成/冲突改名残留」，不要当正式数据。
- 训练：`outputs/train/<job>/checkpoints/<step>/`；Windows 上 `last` 符号链接可能不存在，以数字目录为准。
- 校准：`calibration/robots/so_follower/`、`calibration/teleoperators/so_leader/`。
- 环境：`logs/verification.json`。

## 硬规则（本机）

- 录制/训练默认 `--dataset.push_to_hub=false`、`--policy.push_to_hub=false`、`--wandb.enable=false`。
- 本地数据集训练加 `--dataset.video_backend=pyav`，并写明 `--dataset.root=`（时间戳目录）。
- 串口：Leader=`COM3` / `so101_leader`；Follower=`COM4` / `so101_follower`。变化则更新 `nodes/hardware.md`。
- 不把 token、`.env`、密钥写入 lab-log。

完整模板见 [templates.md](templates.md)。
