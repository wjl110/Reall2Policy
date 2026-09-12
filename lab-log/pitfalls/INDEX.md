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
| P010 | 折叠起始姿态 rollout 只抖动 | 高 |
| P011 | 录制时按 Esc（含 Rerun 窗口）会整段退出 | 中 |
| P012 | 训练读不到刚补采的 mp4（file-002） | 高 |
| P013 | 抓放成功后回折叠，第二轮卡死抖动 | 高 |
| P014 | E03 进度条冻在 24398，step 不再增加 | 高 |
| P015 | 连续多轮后只放不抓 / 夹爪该闭却开 | 高 |
| P016 | 物体在 A、策略去 B 找（位置幻觉） | 高 |
| P017 | Object OOD 夹爪开合与正常夹取相反 | 中 |
| P018 | DAgger 连续录 Ctrl-C 后 0 episode | 高 |

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
- 再现：2026-09-10 03:21 写入 `040000` **成功**，进程未退出（开发人员模式可能已开）。仍以数字目录为准。

### P006 本地数据集训练必须 pyav

- 时间：2026-09-10
- 症状：未指定 backend 时本地 AV1 视频可能踩 TorchCodec。
- 根因：录制视频 `video.codec=av1`，`video_backend=pyav`。
- 解法：训练加 `--dataset.video_backend=pyav`。
- 以后：本机数据集默认 pyav。

### P007 录制热键

本版 LeRobot（非旧教程的 n/r/q 为主）：

- **→**：提前结束当前录制或复位，进入下一集
- **←**：本集作废重录
- **Esc** 或 **q**：结束整次采集（Rerun 窗口里按 Esc 一样会停，见 P011）
- 时间到了会自动进下一集（本批 20s 录 + 8s 复位）


### P008 Windows 不能照抄 Linux 教程

- 串口是 `COM3`/`COM4`，不是 `/dev/ttyACM0`。
- 不要 `sudo`/`apt`/`chmod`。
- 激活用 `activate.cmd`，不要假设 bash。

### P009 GitHub 100MB 与嵌套 git

- `outputs/` 权重超 100MB，已 gitignore。
- `env/`、`cache/` 不上传。
- `lerobot/.git` 会让父仓库把它当 submodule；纳入时需去掉嵌套 git 元数据。
- 仓库创建仍待 `gh auth login`。

### P010 折叠起始姿态 rollout 只抖动

- 时间：2026-09-10 09:53–22:43
- 症状：`lerobot-rollout` 软件正常（30 Hz、150s 跑完），从臂只在折叠收着的姿态附近抖动，不去抓放。
- 根因：训练数据起始都是桌面上方工作姿态；折叠态对模型是 OOD，输出在当前位置附近小幅修正 → 抖动。
- 解法：先 `lerobot-teleoperate` 把从臂摆到与录数据时相同的起始姿态（伸到桌面上方、对着物体），再跑 rollout。对齐后用户确认抓放完全 OK。
- 以后：评估/Demo 前必须复位到录制起始位；物体和摄像头尽量与训练一致。补采时每集也从同一类起始姿态开始。
- 再现：2026-09-11 E02 第二轮从折叠起同样只抖。但第一轮是策略自己折回去的，见 P013。
- 缓解：2026-09-12 E03 开跑前 Demo，用户确认折叠态可以伸出并进入工作态。评估 90 次仍用工作态起步。

### P013 抓放成功后回折叠，第二轮卡死抖动

- 时间：2026-09-11 03:48–03:50
- 症状：E02 `lerobot-rollout` 60s。先成功拿起并放下，然后回到折叠态；第二次起不来，一直在折叠态抖动。软件正常（29.88 Hz，Duration limit 结束）。
- 根因：现有 50 集每集只有一轮 15–20s 抓放，结束常含收臂/折叠。ACT 模仿「做完回家」。折叠态从未作为「再去接近物体」的起始观测（P010）。60s ≈ 3 个 episode 连在一起，没有人工复位。
- 解法（评估）：单次验证用 `--duration=20`，或第一轮成功后 Ctrl-C；要连做必须先遥操摆回工作姿态。Demo 只录第一轮。
- 以后（补采 +50）：结束停在桌面上方工作姿态，不要折臂；部分集一条里连续抓放两次；加几条从折叠回到工作位再抓。
- 不要：为此改训 DP/VLA，或没加数据就重开 E02。
- 缓解：2026-09-12 E03 开跑前 Demo，折叠态可伸出进工作态；计次 90 次未再报回折叠卡死。坑未关（后程改 P015 空放）。

### P011 录制时按 Esc（含 Rerun 窗口）会整段退出

- 时间：2026-09-10 22:58
- 症状：补采做到 episode 24 复位阶段突然停；日志 `Escape key pressed. Stopping data recording...`，不是报错。
- 根因：`pynput` 全局监听。`Esc` 或 `q` = 结束整次录制。Rerun 窗口里按 Esc 同样会停。
- 解法：已录的 5 集已写入（总数 25）。续录同一 root，`--resume=true --dataset.num_episodes=25`（还差 25 到 50）。
- 以后：看画面时不要按 Esc。提前结束当前集用 **→**；重录当前集用 **←**；真要停再用 Esc/`q`。

### P012 训练读不到刚补采的 mp4（file-002）

- 时间：2026-09-10 23:24
- 症状：E02 `lerobot-train` 在 step 614 退出。`RuntimeError: Caught FileNotFoundError in DataLoader worker process 3` → `av.error.FileNotFoundError`，路径 `videos\observation.images.front\chunk-000\file-002.mp4`。不是 Esc，也不是 Rerun 内存告警。
- 根因：`info.json` 已是 50 ep / 27000 帧，但补采视频还在拼接/落盘。`file-000.mp4` 是凌晨第一批（20 ep / 9000 帧，01:19 已在）；`file-001.mp4`（5 ep / 3000 帧）和 `file-002.mp4`（25 ep / 15000 帧）的创建时间都是 **23:24:56**，与崩溃同一秒。训练 23:23:45 开跑时只能稳定读到 `file-000`，shuffle 抽到后半段 episode 就炸。
- 解法：事后三份 mp4 均存在且可解码（合计 27000 帧）。`act_so101_e02` 无数字 checkpoint（`save_freq=20000`），**从头重训**，不要 `--resume`。开训前确认 `chunk-000` 下三个 mp4 都在。
- 以后：录制 Stop 之后先看视频目录时间戳，三个（或当前应有的）mp4 都写完再 `lerobot-train`。不要在 Stop 后立刻开训。

### P014 E03 进度条冻在 24398，step 不再增加

- 时间：2026-09-12 02:23 起（约 10 分钟）
- 症状：`Training: 24% | 24398/100000 [37:58<1:48:54, 11.57step/s]` 不再变。进程还在：`python.exe` PID 42340 + 4 个 DataLoader worker，GPU 约 60–86%，CPU 仍在涨。
- 根因：训练循环卡在下一步（`next(dl_iter)` 或 CUDA/控制台刷新），不是「tqdm 只是不刷屏」。日志文件 8 秒内 `24398` 不变，也没有 `step:26K`。
- 解法：在**真正的训练窗口** Ctrl-C，从已落盘的 20K 恢复：

```bat
lerobot-train --config_path=D:\SO-ARM101\outputs\train\act_so101_e03\checkpoints\020000\pretrained_model\train_config.json --resume=true
```

- 损失：约 4400 step（20K→24K），20K ckpt 完好。不要从头重开，不要覆盖 E02。

### P015 连续多轮后只放不抓 / 夹爪该闭却开

- 时间：2026-09-12 IID 第 4–6 轮
- 症状：前几轮能抓，未松开偏多；第 4 轮第 6 次起夹爪在闭合态张开、抓不到；第 5–6 轮变成空臂放置张合，没有抓的姿态。
- 根因：长会话策略塌缩（与 P013 回折叠同类，但是后程模式崩，不是单次回折叠）。
- 不要：为此现在改训 DP/VLA，或没做完 OOD 就开 DAgger。
- 以后：W7 用 DAgger 补「未松开」和「空放」恢复轨。

### P016 物体在 A、策略去 B 找（位置幻觉）

- 时间：2026-09-12 E03 开跑前 Demo（未计次）
- 症状：物品放在 A，臂去 B 寻找，或搜索点与实物不重合。另有起始位姿对不准。
- 根因：ACT 更像模仿训练轨迹，不是检测物体坐标。90 次 IID 都是夹爪正下方已有物体，会掩盖这个问题。
- 不要：把 37/90 当成任意位置成功率。
- 以后：Position OOD 物体必须离开夹爪正下方；W7 DAgger 在「找错点」时接管。
- 再现：2026-09-12 Position OOD 6×15=90，全部失败。训练扫过区、不在夹下。第 1 轮找失败但能张爪；第 2–6 轮定位失败且夹爪不开。
- 再现：2026-09-12 Object OOD 0/90。半透明盒+牙刷头。近处在附近抓仍找不到；远处空中抓。
- 再现：2026-09-12 Lighting 第 5 轮，夹子正下方未识别并远离物体。

### P017 Object OOD 夹爪开合与正常夹取相反

- 时间：2026-09-12 Object OOD 第 6 轮
- 症状：做成放取动作，找不到目标点，夹爪打开/关闭逻辑与正常夹取相反。
- 根因：后程模式崩（同类 P015），叠加新物体外观。
- 不要：并行 DP/VLA；未采完就训 ACT-v2。
- 以后：W7 DAgger 补开合时序。
- 再现：2026-09-12 Camera 第 6 轮前段取放姿态、逻辑相反；13–15 回正常抓取。

### P018 DAgger 连续录 Ctrl-C 后 0 episode

- 时间：2026-09-12 16:20
- 症状：跑了约 18 分钟、多次纠正，`info.json` 仍是 0 ep / 0 frames，没有 mp4。
- 根因：`record_autonomous=true` 按视频体积切集（默认约 200MB），短会话不切集；Ctrl-C Force shutdown 打断 finally 的 `save_episode`。
- 解法：新开目录；`--strategy.target_video_file_size_mb=15`；停用 **Esc**，等到日志出现 `Episode saved` 或 `Final in-progress episode saved`。不要 Ctrl-C。
- 不要：对着空目录开训。
- 缓解：2026-09-13 `dagger2` + 15MB 切集 + Esc，**14 ep / 37494 帧**落盘；`Final in-progress episode saved`。

