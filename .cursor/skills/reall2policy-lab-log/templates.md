# 台账模板

写入 `lab-log/` 时套用下列结构。可删空节，不可省略「做了什么 / 数据 / 效果」。

## 会话 `lab-log/sessions/YYYY-MM-DD.md`

同一天多次对话追加 `## HH:MM` 小节。

```markdown
# 会话 2026-09-10

## 02:50 启动快照
- 终端：act 训练 resume 中，约 step 22K
- 最新数据：so101_pick_place_20260910_011033（20 ep / 9000 frames）
- 最新权重：checkpoints/020000
- 用户本轮意图：（会话开始时可写「待定」，随后补）

## 过程
- HH:MM 发生了什么 → 效果 → 写入的实验/踩坑文件
```

## 实验 `lab-log/experiments/YYYY-MM-DD_<短名>.md`

```markdown
# 实验：<一句话标题>

- 状态：进行中 | 成功 | 失败 | 中断
- 时间：YYYY-MM-DD HH:MM
- 操作者：用户 / Agent

## 做了什么
目的：
命令：

```bat
<可复现命令>
```

## 实验数据
| 项 | 值 |
|----|----|
| repo_id | |
| root | |
| episodes / frames / fps | |
| 相机 | |
| 任务 | |
| 输出目录 | |

## 效果
- 结果：
- 指标：（loss、step/s、显存、实机成功率）
- 结论：

## 重要日志
```
<精简原文>
```

## 节点
- 硬件：COM / robot.id / GPU
- checkpoint：
- 关联踩坑：
```

## 踩坑（追加到 `pitfalls/INDEX.md` 表格 + 必要时独立小节）

```markdown
### P0xx <短标题>
- 时间：
- 症状：
- 根因：
- 解法：
- 以后：
```

## 图表 `lab-log/metrics.json` + `charts.md`

先改 json 再改 mermaid。四张图：学习进程、项目收益、学习曲线、数据回收。见 Skill 内 `charts-spec.md`。

## 课表实践 `lab-log/course.md`

按周更新「计划 / 实际 / 差距」。每次启动改「当前焦点」；每次练完改对应周。

```markdown
### W2 数据
- 课表：100 episodes
- 实际：20 / 100（root=..._011033）
- 差距：缺 80；补采须等 E01 训完
- 最近一次实践：YYYY-MM-DD 做了什么 → 效果
```

`docs/COURSE.md` 只改顶部状态表数字（如 `20/100`、`~30K/100K`），不要改用户要复制的命令块。

## CURRENT.md 只保留「现在」

只写：课表第几周、正在跑什么、最新可用数据/权重、阻塞点、下一步（来自课表）。历史放到 experiments / sessions / course.md。
