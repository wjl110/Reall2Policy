# Reall2Policy

Windows 上的 SO101 机械臂数据采集、ACT 策略训练与部署环境。基于 Seeed 验证版 [LeRobot](https://github.com/Seeed-Projects/lerobot)。

## 快速开始

1. 克隆本仓库后，按 [使用说明.md](使用说明.md) 准备 Python / CUDA 环境。
2. 双击 `start.cmd` 打开已激活的命令窗口。
3. 运行 `verify.cmd` 检查安装。

## 仓库内容

| 路径 | 说明 |
|---|---|
| `lerobot/` | LeRobot 源码（editable 安装） |
| `calibration/` | SO101 leader / follower 校准数据 |
| `data/` | 本地采集的演示数据集 |
| `activate.cmd` / `start.cmd` | Windows 环境激活与启动 |
| `verify.cmd` / `verify.py` | 环境自检 |
| `使用说明.md` | 完整使用文档 |
| `lab-log/` | 实验与踩坑台账（每次加载项目由 Agent Skill 维护） |

`env/`、`cache/`、训练产物 `outputs/` 体积过大，未纳入 Git。请在本机按使用说明重建环境。

## 许可证

`lerobot/` 目录遵循 Apache 2.0。其余项目文件同样按 Apache 2.0 使用。
