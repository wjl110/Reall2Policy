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

## CURRENT.md 只保留「现在」

只写：正在跑什么、最新可用数据/权重、阻塞点、下一步。历史放到 experiments / sessions。
