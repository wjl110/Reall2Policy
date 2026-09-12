# 实验：W7 DAgger 加采（第一趟）

- 状态：失败（0 episode 落盘）
- 时间：2026-09-12 16:01–16:20
- 课表：W7

## 做了什么

`lerobot-rollout --strategy.type=dagger --strategy.record_autonomous=true`，约 1071s，29.97 Hz。终端可见约 7 次 correcting。Ctrl-C（signal 2 / Force shutdown）。

## 实验数据

| 项 | 值 |
|----|----|
| 目录 | `data/local/rollout_so101_dagger` |
| 磁盘 | 仅 `meta/info.json`（0 ep / 0 frames）+ `tasks.parquet` |
| mp4 / parquet 数据 | 无 |

连续模式按视频体积切集（默认约 200MB），18 分钟未切集；末条应在 finally `save_episode`，被 Force shutdown 打断（P018）。

## 结论

操作做了，数据没落下。重采：新目录、把切集体积降到 15MB、用 Esc 并等到 `Final in-progress episode saved`。先采不训。
