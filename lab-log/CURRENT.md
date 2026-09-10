# 当前状态

更新：2026-09-11 01:13

## 课表

**W3 E02 重训进行中（~58K/100000）。** 训练和录制不要同时进行。不要打断。

## 正在跑

`lerobot-train` → `outputs/train/act_so101_e02`  
step ~58K，loss≈0.086，~9.3 step/s。ckpt `020000`、`040000` 已落盘。

## 最新可用数据

| 项 | 值 |
|----|-----|
| 数据集 | `data/local/so101_pick_place_20260910_011033` |
| 规模 | **50 episodes / 27000 frames** / 30 fps |
| 权重 | E01 `100000`；E02 `020000`/`040000` |
| 真机 | 对齐后抓放成功（P010） |
| README | `sync-readme.py` 从 `metrics.json` 生成进度块 |

## 阻塞 / 未完成

- 训练读 `..._011033`，加采到 100 须等 E02 结束。
- W4 `assets/demo.mp4` 未录；首页并排 `demo.gif` + `demo_0.gif`。

## 下一步（按课表）

等 E02 跑完（100K）。结束后再 +50→100 训 E03。里程碑时跑 `sync-readme.cmd` 并 push。
