# 实验：首次录制试跑

- 状态：部分成功（第三次目录可用）
- 时间：2026-09-10 00:27–00:32
- 操作者：用户

## 做了什么

目的：打通 `lerobot-record` 全链路（相机 + 主从 + 落盘）。

相机：`front` OpenCV index 0，640×480@30。默认曾尝试 push Hub → 401（P002）。

## 实验数据

| 目录 | episodes | frames | 说明 |
|------|----------|--------|------|
| so101_first_test_20260910_002706 | 1 | 300 | 试录 |
| so101_first_test_20260910_002752 | 1 | 300 | 试录 |
| so101_first_test_20260910_003232 | 1 | 300 | **完整试录，replay 用这个** |

视频：AV1，pyav，30 fps。robot_type=`so_follower`。

回放应带 root：

```bat
lerobot-replay --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --dataset.repo_id=local/so101_first_test --dataset.root=D:\SO-ARM101\data\local\so101_first_test_20260910_003232 --dataset.episode=0
```

## 效果

录制本体成功；Hub 上传失败不影响本地文件。同名目录被改成时间戳（P003）。夹爪有过载风险（P004）。

## 节点

关联：P002、P003、P004。
