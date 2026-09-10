# Scripts

常用命令在 `docs/COURSE.md`。

## README 同步

- `sync-readme.py`：读 `lab-log/metrics.json` 的 `readme` 段，写入 `README.md` 的 `<!-- readme:* -->` 标记块。
- 根目录 `sync-readme.cmd` 一键运行（需先 `activate.cmd`）。
- Agent 在里程碑或应对外 push 前更新 `metrics.json` 后执行。

## 计划中的脚本

- `evaluation/`：`evaluate.py`、`generalization.py`、`failure_analysis.py`（W5 起）
- `deployment/`：封装 `lerobot-rollout`（W4 起）
