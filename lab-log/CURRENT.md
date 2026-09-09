# 当前状态

更新：2026-09-10 02:50

## 正在跑

ACT 训练 **resume 中**（终端 `cmd /k activate.cmd`）。

- 命令：`lerobot-train --config_path=outputs/train/act_so101_pick_place/checkpoints/020000/pretrained_model/train_config.json --resume=true`
- 目标：100000 step；已有 ckpt **020000**；启动时从 epoch 17 / sample 7000 续跑
- 02:50 日志约 **step 22K**，loss≈0.121，l1≈0.107，~9.6 step/s，显存 2.10 GB
- 输出：`outputs/train/act_so101_pick_place`

## 最新可用数据

| 项 | 值 |
|----|----|
| 数据集 | `data/local/so101_pick_place_20260910_011033` |
| repo_id | `local/so101_pick_place` |
| 规模 | 20 episodes / 9000 frames / 30 fps / 640×480 AV1 |
| 任务 | Pick up the object and place it down. |
| 权重 | `outputs/train/act_so101_pick_place/checkpoints/020000` |

## 阻塞 / 未完成

- 训练未到 100K；存盘依赖「开发人员模式」否则会再撞 P005。
- GitHub 仓库 `Reall2Policy` 尚未创建：等用户完成 `gh auth login`（上次验证码已过期）。
- 实机 `lerobot-eval` 尚未做。

## 下一步

1. 让训练跑完 100K（或至少再存 040000）。
2. 实机评估 ACT。
3. 用户登录 GitHub 后创建并推送 `Reall2Policy` 仓库。
