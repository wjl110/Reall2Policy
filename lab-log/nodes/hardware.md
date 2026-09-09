# 硬件与环境节点

更新：2026-09-10

## 机械臂

| 角色 | 类型 | 端口 | id | 校准文件 |
|------|------|------|-----|----------|
| Leader 主臂 | `so101_leader` | **COM3** | `so101_leader` | `calibration/teleoperators/so_leader/so101_leader.json` |
| Follower 从臂 | `so101_follower` | **COM4** | `so101_follower` | `calibration/robots/so_follower/so101_follower.json` |

从臂关节：shoulder_pan=1, shoulder_lift=2, elbow_flex=3, wrist_flex=4, wrist_roll=5, gripper=6。`use_degrees=true`。

## 相机

- 前端：OpenCV UVC，`index_or_path=0`，640×480@30
- OpenCV 为 headless，`cv2.imshow` 不可用，可视化用 Rerun

## 计算节点

| 项 | 值 |
|----|----|
| 本机目录 | `D:\SO-ARM101`（项目名 Reall2Policy，文件夹暂未改） |
| Python | 3.12.14（`env\`） |
| LeRobot | 0.6.2（Seeed，editable） |
| PyTorch | 2.10.0+cu128 |
| GPU | RTX 5060 Ti 8GB，CUDA 12.8，capability 12.0 |
| FFmpeg | 7.1.1 + libsvtav1 |
| 驱动 | NVIDIA 591.74 |
| 激活 | `call activate.cmd` 或双击 `start.cmd` |

环境自检：`logs/verification.json`（2026-09-08 软件通过，当时硬件未接）。

## 常用路径

- 数据：`D:\SO-ARM101\data`（`HF_LEROBOT_HOME`）
- 校准：`D:\SO-ARM101\calibration`
- 训练输出：`D:\SO-ARM101\outputs\train\`
