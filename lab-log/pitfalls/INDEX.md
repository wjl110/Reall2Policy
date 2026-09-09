# 踩坑索引

按编号追加，不要删旧条。再现时在原条下加「再现：日期 + 一句话」。

| ID | 标题 | 严重度 |
|----|------|--------|
| P001 | 串口 openPort 失败 / 端口被占用 | 高 |
| P002 | 默认上传 Hugging Face 导致 401 | 高 |
| P003 | 同名数据集被改成带时间戳目录 | 高 |
| P004 | 夹爪舵机 id=6 Overload | 高 |
| P005 | WinError 1314 无法创建 checkpoints/last 符号链接 | 高 |
| P006 | 本地数据集训练必须 pyav，不能默认 TorchCodec | 中 |
| P007 | 录制热键：n/r/q 不是每帧都按 | 低 |
| P008 | Windows 不能照抄 Linux 教程路径与命令 | 中 |
| P009 | GitHub 单文件 100MB；lerobot 嵌套 .git | 中 |

---

### P001 串口 openPort 失败 / 端口被占用

- 时间：2026-09-10 00:09
- 症状：`lerobot-calibrate --robot.port=COM4` 在 `motors_bus.py _connect` → `openPort()` 失败。
- 根因：COM 口被其他窗口占用、线没插稳、或校准窗口与遥操窗口抢同一端口。
- 解法：关掉所有占用 COM3/COM4 的进程；设备管理器确认两张板；拔插后 `lerobot-find-port`。校准后来已成功。
- 以后：同时只开一个操作该口的命令；新窗口先 `call activate.cmd`。

### P002 默认上传 Hugging Face 导致 401

- 时间：2026-09-10
- 症状：录制本体成功，结束后因 push Hub 401 看起来像整段失败。
- 根因：`lerobot-record` 默认 `push_to_hub=true`，未登录 HF。
- 解法：一律加 `--dataset.push_to_hub=false`。训练加 `--policy.push_to_hub=false --wandb.enable=false`。
- 以后：未 `huggingface-cli login` 不要开上传。

### P003 同名数据集被改成带时间戳目录

- 时间：2026-09-10
- 症状：`replay` / `train` 找不到 `so101_first_test` 或 `so101_pick_place`；实际在 `*_YYYYMMDD_HHMMSS`。
- 根因：目标目录已存在时 LeRobot 自动改名；空壳目录也会占名。
- 解法：所有后续命令带 `--dataset.root=D:\SO-ARM101\data\local\<实际目录>`。以 `meta/info.json` 里 episodes>0 的为准。
- 以后：INDEX 里维护「实际 root」；不要假设 repo_id 等于文件夹名。

### P004 夹爪舵机 id=6 Overload

- 时间：2026-09-10（遥操/回放阶段）
- 症状：夹爪过载报警，动作中断。
- 根因：夹爪死顶桌面或堵转。
- 解法：断电休息；手动把臂摆到中间；主臂不要压桌；失败 episode 按 `r` 重录。
- 以后：下降到物体附近再夹，夹稳再抬；不要边走边用爪撑桌子。

### P005 WinError 1314 无法创建 checkpoints/last 符号链接

- 时间：2026-09-10 约 02:37（训练到 20K 存盘）
- 症状：loss 正常下降，存 020000 后因创建 `checkpoints\last` 失败导致进程退出。
- 根因：Windows 默认禁止普通用户建目录符号链接。
- 解法：设置 → 系统 → 开发者选项 → **开发人员模式**；然后  
  `lerobot-train --config_path=outputs/train/act_so101_pick_place/checkpoints/020000/pretrained_model/train_config.json --resume=true`  
  权重本身是完整的，以数字目录为准，不要依赖 `last`。
- 以后：新机器先开开发人员模式再训；或管理员运行 `start.cmd`。

### P006 本地数据集训练必须 pyav

- 时间：2026-09-10
- 症状：未指定 backend 时本地 AV1 视频可能踩 TorchCodec。
- 根因：录制视频 `video.codec=av1`，`video_backend=pyav`。
- 解法：训练加 `--dataset.video_backend=pyav`。
- 以后：本机数据集默认 pyav。

### P007 录制热键

- `n`：提前结束当前录制或复位，进入下一步（不是每帧都按）。
- `r`：本集作废重录。
- `q`：结束整次采集。
- 回放不用按 `n`，看完 `Ctrl+C`。
- 时间到了会自动进下一集（本实验 15s 录 + 5s 复位）。

### P008 Windows 不能照抄 Linux 教程

- 串口是 `COM3`/`COM4`，不是 `/dev/ttyACM0`。
- 不要 `sudo`/`apt`/`chmod`。
- 激活用 `activate.cmd`，不要假设 bash。

### P009 GitHub 100MB 与嵌套 git

- `outputs/` 权重超 100MB，已 gitignore。
- `env/`、`cache/` 不上传。
- `lerobot/.git` 会让父仓库把它当 submodule；纳入时需去掉嵌套 git 元数据。
- 仓库创建仍待 `gh auth login`。
