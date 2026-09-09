# 实验：校准 + 遥操打通

- 状态：成功
- 时间：2026-09-10 00:09 起
- 操作者：用户

## 做了什么

目的：给 Leader/Follower 写校准，确认主从跟随。

```bat
lerobot-calibrate --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower
```

Leader 侧对应 COM3 / `so101_leader`。随后遥操（具体命令以当时窗口为准）已跑通。

## 实验数据

校准产物：

- `calibration/robots/so_follower/so101_follower.json`
- `calibration/teleoperators/so_leader/so101_leader.json`

## 效果

- 00:09 第一次 calibrate 因 `openPort()` 失败（P001）。
- 之后校准文件已生成，遥操可用，进入录制阶段。

## 重要日志

```
calibrate.py:89  robot.port=COM4  id=so101_follower  use_degrees=True
Traceback: motors_bus.py _connect → openPort() failed
```

## 节点

- Follower COM4；Leader COM3
- 关联：P001、P004、P008
