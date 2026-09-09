# 实验：建立实验台账 Skill

- 状态：成功
- 时间：2026-09-10 02:50
- 操作者：Agent（用户要求）

## 做了什么

目的：从现在起自动记录全部实验与踩坑；每次加载项目启动该 Skill。

落地：

- 记录目录 `lab-log/`
- 项目 Skill `.cursor/skills/reall2policy-lab-log/`（可被模型自动调用）
- 始终生效规则 `.cursor/rules/reall2policy-lab-log.mdc`
- 根目录 `AGENTS.md`

## 实验数据

无机械臂数据。台账已回填 2026-09-08 至今的环境、校准、录制、训练与踩坑。

## 效果

之后每次新对话应先读 CURRENT/INDEX/course、写会话快照、汇报状态。实验/报错发生时立刻落盘。

03:03 追加：对照 `docs/COURSE.md` 跟踪学习实践（周次、计划 vs 实际、禁止跳周）。

## 节点

见 `lab-log/INDEX.md`。
