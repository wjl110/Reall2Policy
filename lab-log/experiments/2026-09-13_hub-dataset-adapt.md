# Hub 开放数据 / 权重对本机 SO-101 的适配

- 状态：结论已确认，未下载、未混训
- 时间：2026-09-13 13:54
- 课表：W7（只调研，不跳周）
- 对照：[LeRobot 文档](https://huggingface.co/docs/lerobot/main/en/index)、[Imitation Learning](https://huggingface.co/docs/lerobot/il_robots)

## 做了什么

对照官方 LeRobot 文档与 Hub 上 `lerobot/` 组织的开放数据集、开放权重，核对本机 `so101_pick_place` / `so101_v3_mix` 的 schema（相机键、关节名、fps、版本、校准域）。

## 本机锚点

| 项 | 值 |
|----|-----|
| 格式 | LeRobotDataset **v3.0** |
| robot_type | `so_follower` |
| 关节 | 6：`shoulder_pan.pos` … `gripper.pos` |
| 相机 | 仅 `observation.images.front`，640×480@30 |
| 动作范围（100 ep） | pan −93~44°；wrist_roll ±180°；夹爪 0~62 |
| 任务 | `Pick up the object and place it down.` |
| ACT 输入 | 只认 `front`（见 `act_so101_v3` config） |

## 官方数据

| repo | ep / 帧 | 版本 | robot_type | 关节名 | 相机 | 对本机 |
|------|---------|------|------------|--------|------|--------|
| [lerobot/svla_so101_pickplace](https://huggingface.co/datasets/lerobot/svla_so101_pickplace) | 50 / 11939 | v2.1 | `so100_follower` | **同名** 6 轴 | **`up` + `side`** | 能加载；不能直接混 ACT |
| [lerobot/svla_so100_pickplace](https://huggingface.co/datasets/lerobot/svla_so100_pickplace) | 50 / 19631 | v2.1 | `so100` | `main_*` | `top` + `wrist` | 关节名也不对齐 |
| svla_so100_stacking / sorting | 官方同系列 | v2.1 | SO-100 | 非本任务 | 多相机 | 任务域不同 |

官方教程明确：Hub 上的 LeRobotDataset 可直接 `--dataset.repo_id=` 训练；策略会按**该数据集**的电机数和相机数建网。真机部署时相机名必须一致。SmolVLA 示例推理相机是 `up` + `side`。

## 开放权重

| 权重 | 用途 | 对本机 |
|------|------|--------|
| [lerobot/smolvla_base](https://huggingface.co/lerobot/smolvla_base) | 官方 base，要在自己数据上微调 | **W9 该用**；不要现在开 |
| π₀ / π₀.₅ | 更大 VLA | 8GB 显存不合适 |
| 官方 ACT 针对本机单 `front` | 未见同配置公开 ckpt | 无即插即用 ACT |

`smolvla_base` 的示例微调数据就是 `lerobot/svla_so101_pickplace`。

## 适配性（结论）

1. **格式层：能用。** 同一套 LeRobotDataset，本机 0.6.2 可 `LeRobotDataset("lerobot/svla_so101_pickplace")` 或 `lerobot-train --dataset.repo_id=...`。
2. **ACT 混训 / 当本机示教：不能用。** 相机键 `up`/`side` ≠ `front`；校准零位、桌面、物体、机位都不同。别人的关节角不能当本机动作。混进 `so101_v3_mix` 会把 v3 训废。
3. **回放官方集到 COM4：不能用。** 同理由。
4. **W9 SmolVLA：该用权重，不是该混官方集。** `--policy.path=lerobot/smolvla_base`，数据仍用本机（语言指令另采）。相机不够可用官方 `rename_map` / `empty_cameras`，但 fine-tune 必须吃本机画面。
5. **社区 so101 集：** 大量 1–15 ep 教程、双相机、50 Hz、腕部相机或视频未上传。不当 W7 补集。

## 效果 / 决定

- 不下载、不混 `so101_v3_mix`、不开第二路训练。
- ACT-v3 继续只吃本机 111 ep。
- Hub 数据留到 W9 当「怎么微调」的对照，不当本周数据飞轮。

## 节点

- 调研时 ACT-v3 已有 `020000`（13:11 开训）。20K loss 未采到，不编造。
- 本机不上 Hub（P002）；只读 Hub 不需要 write token。
