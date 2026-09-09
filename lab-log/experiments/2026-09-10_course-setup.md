# 实验：12 周课表落地

- 状态：成功
- 时间：2026-09-10 02:54
- 操作者：Agent

## 做了什么

目的：按求职级 12 周路线把本机命令写进仓库，用户只复制执行。

产物：

- `docs/COURSE.md`（唯一操作手册）
- `docs/dataset.md`、`configs/{act,diffusion,smolvla}.yaml`
- `experiments/INDEX.md`（E01–E08）
- `results/eval_template.md`、`results/act_vs_dp.md`
- `data/README.md`、`scripts/README.md`、`assets/.gitkeep`
- `README.md` 改成作品集第一屏

未改训练进程。未新建 GitHub 远程（仍待 `gh auth login`）。

## 实验数据

| 项 | 值 |
|----|-----|
| 课表锚点 | W2=20/100 ep，W3=ACT ~24K/100K |
| 任务 | Pick up the object and place it down. |

## 效果

- 结果：课表已可按周执行
- 结论：下一步是等 E01 训完再补采，不并行 DP/VLA

## 节点

- 关联：当前 ACT resume、P005
