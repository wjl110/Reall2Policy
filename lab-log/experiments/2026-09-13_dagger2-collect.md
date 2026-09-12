# 实验：W7 DAgger 重采 dagger2

- 状态：成功（采集完成，未训）
- 时间：2026-09-13 约 01:30–02:22
- 课表：W7

## 做了什么

官方 DAgger 连续录：`--strategy.type=dagger --strategy.record_autonomous=true --strategy.target_video_file_size_mb=15`。Esc 停，等到 `Final in-progress episode saved`。

## 实验数据

| 项 | 值 |
|----|----|
| 目录 | `data/local/rollout_so101_dagger2` |
| episodes / frames / fps | **14 / 37494 / 30** |
| 纠正 | **61 段 / 12942 帧（34.5%）**；中位 6.2s，最短 2.4s，合计 431s |
| 视频 | `file-000`～`file-012.mp4`（与 episodes meta 一致） |
| parquet | `data/chunk-000/file-000.parquet` |
| 控制 | 整段 29.96 Hz；49811 ticks |
| 残段 | ep8 8.2s、ep13 3.1s，无纠正（切集/Esc） |

P018 已绕过：15MB 切集，Esc 正常收尾。

## 效果

- 落盘完整，可训。
- 纠正次数超过约定 30–50。
- 不能 resume 进原 100 ep（多 `intervention`）。
- 全量训会带上约 65% 策略自跑帧。

## 重要日志

```
02:22:23 Episode saved (total: 13, elapsed: 136.6s)
02:22:26 Stop recording...
02:22:26 Final in-progress episode saved
02:22:30 Rollout finished
```

## 节点

- Leader COM3 / Follower COM4 / 相机 front 640×480@30
- 策略：E03 `checkpoints/100000`
- 关联：P018
