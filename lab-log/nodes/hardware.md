# 硬件与环境节点

更新：2026-09-12

## 机械臂

| 角色 | 类型 | 端口 | id | 校准文件 |
|------|------|------|-----|----------|
| Leader 主臂 | `so101_leader` | **COM3** | `so101_leader` | `calibration/teleoperators/so_leader/so101_leader.json` |
| Follower 从臂 | `so101_follower` | **COM4** | `so101_follower` | `calibration/robots/so_follower/so101_follower.json` |

从臂关节：shoulder_pan=1, shoulder_lift=2, elbow_flex=3, wrist_flex=4, wrist_roll=5, gripper=6。`use_degrees=true`。

## 相机

- 前端：OpenCV UVC `index_or_path=0`，软件 **640×480@30**，特征名 `front`
- 设备名：`icspring camera`（USB `VID_2993` `PID_0858`）。仓库与驱动都未写视场角；这类 UVC 常见宣传对角约 70–90°，**本机未标定，不能当规格**
- 无腕部相机。现有 100 ep / E03 只有 `observation.images.front`
- OpenCV 为 headless，`cv2.imshow` 不可用，可视化用 Rerun

## 计算节点

| 项 | 值 |
|----|----|
| 本机目录 | `D:\SO-ARM101`（项目名 Reall2Policy，文件夹暂未改） |
| Python | 3.12.14（`env\`） |
| LeRobot | 0.6.2（Seeed，editable） |
| PyTorch | 2.10.0+cu128 |
| GPU | RTX 5060 Ti 8GB，CUDA 12.8 / 驱动报 CUDA 13.1，capability 12.0 |
| CPU | Intel Core i7-14650HX，16 核 / 24 线程 |
| 内存 | 32 GB（约 31.7 GB 可见） |
| 驱动 | NVIDIA 591.74 |
| 激活 | `call activate.cmd` 或双击 `start.cmd` |

快照 2026-09-10 23:47（E02 训练中）：GPU 占用 93%、5347/8151 MiB、68°C、135W/180W、风扇 45%；CPU 约 30–40%；内存剩余约 10.8 GB。计算进程：`env\python.exe`。另有 `rerun.exe` 仍占显示。

快照 2026-09-12 02:06（E03 bf16）：GPU 占用 85–91%、4048/8151 MiB、67°C、**125–127W / 180W**、SM 2797/3090 MHz。计算进程：`env\python.exe`。桌面进程（Cursor/Chrome/Edge/ToDesk 等）以 C+G 分走部分显存。ACT + batch=8 **喂不饱** 5060 Ti：功耗到不了 180W，利用率到不了 100%。

环境自检：`logs/verification.json`（2026-09-08 软件通过，当时硬件未接）。

## 常用路径

- 数据：`D:\SO-ARM101\data`（`HF_LEROBOT_HOME`）
- 校准：`D:\SO-ARM101\calibration`
- 训练输出：`D:\SO-ARM101\outputs\train\`
