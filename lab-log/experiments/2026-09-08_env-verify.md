# 实验：Windows 环境安装与 verify

- 状态：成功
- 时间：2026-09-08
- 操作者：用户 / 安装脚本

## 做了什么

目的：在原生 Windows 上搭好 Seeed LeRobot + SO101 软件栈，不驱动硬件。

命令：`verify.cmd`（内部跑 `verify.py`）

## 实验数据

无采集数据。依赖快照：`logs/pip-freeze.txt`、`logs/conda-explicit.txt`。

## 效果

软件自检通过：包版本、SO101 CLI 注册、CUDA 矩阵乘、FFmpeg AV1、TorchCodec 回读、teleoperate/record/calibrate/train help、`pip check`。

硬件当时未连接。

## 重要日志

见 `logs/verification.json`：Python 3.12.14，lerobot 0.6.2，torch 2.10.0+cu128，GPU RTX 5060 Ti，`matrix_test: passed`。

## 节点

见 `lab-log/nodes/hardware.md`。
