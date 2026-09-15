# 实验：W7 DAgger dagger3（v3 加采）

- 状态：成功
- 时间：2026-09-13 12:35–13:06
- 课表：W7

## 做了什么

底策略 E03，新目录 `rollout_so101_dagger3`。15MB 切集。Esc 停，`Final in-progress episode saved` + `Rollout finished`。

## 实验数据

| 项 | 值 |
|----|----|
| 目录 | `data/local/rollout_so101_dagger3` |
| episodes / frames / fps | **11 / 33623 / 30** |
| 纠正 | **73 段 / 12571 帧（37.4%）** |
| 视频 | `file-000`～`file-010.mp4` |
| 残段 | ep10 约 11.8s，0 纠正（Esc 尾巴） |
| 墙钟 | 约 1220s（20 min） |

## 效果

- 落盘完整。用户只看到最后两次 saved（`total: 10` + Final），磁盘是 11 集。
- 纠正 73 次，超过目标 30–50。
- 后台 push Hub 401（P002），不影响本地。
- 先不训。下一步混 100 ep 开 `act_so101_v3`。
