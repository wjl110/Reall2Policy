# W8_EXPERIMENT.md

> 权威实验记录（W8 / E07）。本文件只作文档；不修改训练进程。
> 最近巡检时间：2026-09-14 23:37（机器本地时间）

---

## 标准字段

| 字段 | 内容 |
|------|------|
| Experiment ID | W8 / E07 (`dp_so101_v1`) |
| Objective | 同一 100 ep 专家集上训练 Diffusion Policy，完成后与 ACT E03 真机对照（`results/act_vs_dp.md`） |
| Policy | Diffusion Policy（`policy.type=diffusion`，EMA 开启） |
| Dataset | `local/so101_pick_place` → `D:\SO-ARM101\data\local\so101_pick_place_20260910_011033` |
| Dataset size | 100 episodes / 65100 frames / 约 472.64 MB；`robot_type=so_follower`；fps=30；LeRobot dataset v3.0 |
| Training configuration | 见下方「观察到的事实」CLI 与 `configs\diffusion.yaml` |
| Start time | 进程创建时间 2026-09-13 19:50:43–19:50:44（cmd / lerobot-train / python） |
| Training status | **进行中**（进程存活；GPU 占用中） |
| Training duration | 见「推导计算」 |
| Checkpoint | 已有 `020000` / `040000` / `060000` / `last`→060000；尚未见到 `080000` / `100000` |
| Evaluation setup | 训练结束后按 rollout 协议：checkpoint → load → 校验相机/机器人 → **等待批准** → 15×N → 成功/碰到/空抓/抖动/错位；对照基线 ACT E03 |
| Trials / Successes / Failures / Success rate | 本 W8 DP **尚未真机评估**（未知/未开始） |
| Failure categories | 未开始 |
| Observations | 见「观察到的事实」 |
| Hypothesis | 见「假设」 |
| Recommended next experiment | 见文末建议（需你批准后执行） |

---

## 1. 观察到的事实（Observed facts）

### 1.1 当前策略 / 模型

- 命令行明确：`--policy.type=diffusion`，`--ema.enable=true`
- Job：`dp_so101_v1`
- 输出目录：`D:\SO-ARM101\outputs\train\dp_so101_v1`
- 训练环境：`D:\SO-ARM101\env\python.exe`；LeRobot 0.6.2（editable：`D:\SO-ARM101\lerobot`）
- 证据：进程 PID 5856/5828/64204 的 CommandLine；`configs\diffusion.yaml`；`lab-log\experiments\2026-09-13_dp-train.md`

### 1.2 数据集

- `--dataset.repo_id=local/so101_pick_place`
- `--dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033`
- `--dataset.video_backend=pyav`
- `meta\info.json`：`total_episodes=100`，`total_frames=65100`，`fps=30`，`robot_type=so_follower`，`codebase_version=v3.0`
- 目录体积约 **472.64 MB**

### 1.3 训练配置（来自存活进程 CLI）

```text
lerobot-train
  --dataset.repo_id=local/so101_pick_place
  --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033
  --dataset.video_backend=pyav
  --policy.type=diffusion
  --ema.enable=true
  --output_dir=outputs/train/dp_so101_v1
  --job_name=dp_so101_v1
  --policy.device=cuda
  --wandb.enable=false
  --policy.push_to_hub=false
  --batch_size=8
  --steps=100000
  --accelerator.mixed_precision=bf16
```

`configs\diffusion.yaml` 与上表一致，并注明 `eval_weights: pretrained_model_ema`。

### 1.4 进程状态

| PID | 名称 | 创建时间 | 角色 |
|-----|------|----------|------|
| 5856 | cmd.exe | 2026-09-13 19:50:43 | 启动包装 |
| 5828 | lerobot-train.exe | 2026-09-13 19:50:44 | 入口 |
| 64204 | python.exe（SO-ARM101\env） | 2026-09-13 19:50:44 | 主训练进程（CPU 时间很高） |
| 39112/48032/58468/61628 | python.exe workers | 2026-09-13 19:50:54 | multiprocessing workers |
| 59464 | python.exe（application\code） | 2026-09-13 20:23:18 | `scripts\watch-train.py --job dp_so101_v1` |

巡检时以上训练相关进程均存在；**未**对其发送停止/重启。

### 1.5 GPU

- 设备：NVIDIA GeForce RTX 5060 Ti
- `nvidia-smi`（约 23:37）：利用率 **100%**，显存 **~7855–7857 / 8151 MiB**，温度 ~61°C，功耗 ~60–70 W
- `train-live.json` 同期：`gpu_util_pct=100`，`vram_used_mb≈7856`

### 1.6 当前 step / loss（来自状态文件）

来源：`D:\SO-ARM101\lab-log\train-live.json`（`updated` 约 2026-09-14 23:37:15）：

- `step`: **60000**
- `target_step`: **100000**
- `loss`: **0.021**
- `last_ckpt`: **60000**（`last_ckpt_time`: 2026-09-14 17:18:34）
- `alive=true`，`healthy=true`
- `sec_per_step`: 1.3（状态文件中的字段）

早期 loss 采样（`lab-log\metrics.json` → `learning_curve_dp` 与 `2026-09-13_dp-train.md`，开训当晚）：

| step | loss |
|------|------|
| 200 | 0.564 |
| 400 | 0.112 |
| 600 | 0.083 |
| 800 | 0.053 |
| 1000 | 0.047 |
| 2080 | 0.032 |

checkpoint `060000\training_state\training_step.json` 记录 `step: 60000`（与 last ckpt 一致）。

### 1.7 已有 checkpoint

路径：`D:\SO-ARM101\outputs\train\dp_so101_v1\checkpoints\`

| 名称 | LastWriteTime |
|------|----------------|
| 020000 | 2026-09-14 03:13:59 |
| 040000 | 2026-09-14 10:31:38 |
| 060000 | 2026-09-14 17:18:34 |
| last（链接到 060000） | 2026-09-14 17:18:36 |

每个 step 含 `pretrained_model` 与 `pretrained_model_ema`。

### 1.8 磁盘

| 盘 | 总容量 | 剩余 |
|----|--------|------|
| C: | 300 GB | **~12.76 GB**（紧张） |
| D: | ~651.65 GB | **~285.23 GB**（项目所在盘） |

项目侧大约：`outputs\` ~29 GB（其中 `dp_so101_v1` ~15 GB），`data\` ~2 GB，`cache\` ~7 GB，`env\` ~6 GB。

### 1.9 异常信号（仅观察，未处置）

- **有利**：训练进程树完整；主进程 CPU 累计很高；GPU 持续高占用；watcher 仍在更新 `train-live.json` 的时间戳与 GPU 字段。
- **需关注**：`train-live.json` 的 `step` 仍停在 **60000**，且 `last_ckpt_time` 为 **17:18:34**，而巡检时刻约 **23:37**（间隔约 6 小时）。在此期间若按 1.3 s/step 前进，步数应明显高于 60k，但状态文件未体现新的 step，也尚未出现 `080000` checkpoint。
- wandb 关闭；输出目录下未见独立 train `.log` 文件（指标主要依赖 watcher / 历史笔记）。

---

## 2. 推导计算（Derived calculations）

- 进度（按状态文件 step）：60000 / 100000 = **60%**
- 已运行墙钟（按进程创建 → 2026-09-14 23:37）：约 **27 小时 46 分钟**
- 若采用状态文件 `sec_per_step=1.3` 与剩余 40000 step：ETA ≈ 40000 × 1.3 = **52000 s ≈ 14h27m**；`finish_at` 字段约 **2026-09-15 14:03**
- checkpoint 间隔（mtime）：20k→40k ≈ 7.3 h；40k→60k ≈ 6.8 h（与 ~1.2–1.3 s/step 量级相符）
- 开训初期 loss：0.564 @200 → 0.032 @2080（快速下降）；状态文件当前 loss **0.021 @60k 声称值**（若 step 上报滞后，则该 loss 对应的真实 step 不确定）

---

## 3. 假设（Hypotheses）

1. **主假设（良性）**：训练仍在 60k→80k 之间正常前进，但 `watch-train.py` 对 tqdm/`step` 的解析在 60k 之后未更新，导致 `train-live.json` 的 step/loss/ETA 冻结；GPU 100% 支持“仍在算”。
2. **备选假设（异常）**：优化循环在 60k checkpoint 附近卡住（例如数据加载/同步），GPU 仍被占用但 step 不再增加；需在**不杀进程**前提下用只读方式核对（例如下一次是否准时出现 `080000`，或短时观察 GPU 功耗/利用率是否单调空转）。
3. 按课表，日常演示仍应以 **ACT E03** 为准；W8 完成前不宜开 VLA / 不宜在训练中录数或乱 resume（与 `CURRENT.md` / dp-train 笔记一致）。

---

## 4. 未知信息（Unknown information）

- 此时刻**真实** optimizer step 是否 > 60000（缺少新鲜 tqdm/控制台 log 证据）
- 60k 之后完整 loss 曲线（无连续 log；仅有早期曲线 + 状态文件单点 0.021）
- 下一个 checkpoint `080000` 的精确落地时刻
- 本 DP 跑的真机 Trials / 成功率 / 失败分类（尚未评估）
- `last` 符号链接在 Windows 上的完整解析细节（已知存在 `last` 目录项且指向 060000 时段）

---

## 5. 健康判断（摘要）

| 项 | 判断 |
|----|------|
| 进程 | 存活 |
| GPU | 高占用，与训练一致 |
| Checkpoint | 20k/40k/60k 已落盘，间隔合理 |
| 监控 step | **可能滞后** — 需继续只读观察是否出现 80k |
| 磁盘 | D: 充足；**C: 仅约 12.8 GB，风险** |
| 自动处置 | **无**（按要求未 restart/kill/modify） |

---

## 6. 建议的下一步（仅建议，需批准）

1. 保持 `dp_so101_v1` 不动；只读盯 `080000` 是否在约 7h 量级出现。
2. 若长时间无新 checkpoint 且 step 仍死锁，再做更深只读诊断（仍不杀进程），由你决定是否干预。
3. 训练到 `100000` 后：按 [Robotics Policy Rollout Eval] 协议，用 `pretrained_model_ema`，与 E03 对照写 `results/act_vs_dp.md`。
4. 关注 C: 空间；清理须你明确批准。

---

## 7. 记录元数据

- 机器：健霖的台式电脑（已注册本地通道）
- 项目根：`D:\SO-ARM101`
- 本记录路径：`D:\SO-ARM101\lab-log\W8_EXPERIMENT.md`
- 关联：`lab-log\CURRENT.md`、`lab-log\train-live.json`、`experiments\INDEX.md`、`lab-log\experiments\2026-09-13_dp-train.md`
- 巡检约束：未安装、未修改、未杀死、未重启任何训练相关进程

---

## 状态快照 2026-09-14 23:45

### 观察到的事实
- train-live.json updated=2026-09-14 23:45:13；alive=true；healthy=true
- step 仍为 60000；loss=0.021；last_ckpt=60000 @ 17:18:34；尚无 080000
- 进程仍在：5856 cmd / 5828 lerobot-train / 64204 python（主训）/ 59464 watch-train
- nvidia-smi：GPU 100%，7856/8151 MiB，60°C，62.4 W
- 磁盘：C 剩余 12.73 GB；D 剩余 285.23 GB

### 推导
- 自 last_ckpt 已过约 6.4 h；历史 20k 间隔约 6.8–7.3 h，故 80k 窗口将近或已应出现
- 状态文件 ETA finish_at≈2026-09-15 14:11（依赖可能滞后的 step=60k）

### 假设
- 仍偏向「训练在 60k→80k 之间，watcher 的 step 未刷新」；若再过约 1–2 h 仍无 080000，则卡死嫌疑上升

### 健康
- 进程+GPU：看起来在跑
- step/ckpt 上报：需关注（可能滞后）
- 未对训练做任何修改

---

## 状态快照 2026-09-14 23:57

### 观察到的事实
- 磁盘 ckpt 仍为 020000 / 040000 / 060000（mtime 03:13 / 10:31 / 17:18）；尚无 080000
- 训练进程仍在：5856 cmd / 5828 lerobot-train / **64204 python 占 GPU**
- nvidia-smi：GPU ~93%，7673/8151 MiB，60°C，~51 W
- 主进程 UserModeTime 约 1.28e5 s（多核累计，与「还在算」相符）
- 控制台 capture 的 tqdm 停在 **14295**（约 9/14 00:44 的 INFO 14K）；之后只靠 ckpt 判断进度
- train-live.json 的 step=60000 是 `max(ckpt, 过期 tqdm)`，不是证明卡在 60K
- C: 剩余约 11.6 GB；D: 约 285 GB

### 推导
- 20K 间隔：20→40 ≈ 7.3 h，40→60 ≈ 6.8 h。60→80 按 6.8 h 估落地 **约 9/15 00:06**
- 巡检 23:57 距 17:18 约 6.6 h，**尚未超过历史间隔**
- 若按 1.3 s/step 从 60K 匀速，此刻真实 step 应接近 78–80K

### 假设
- 主假设：60K→80K 正常前进，监控滞后
- 若过 00:30 仍无 080000，卡死嫌疑上升（仍不要杀进程，先只读再决定）

### 健康
- 进程 + GPU：正常在跑
- 进度：按 ckpt 节奏正常；大屏数字偏保守
- 未对训练做任何修改

---

## 状态快照 2026-09-15 00:05（loss 预期）

### 观察到的事实
- 磁盘仍无 080000（距 060000 约 6.8 h，窗口边缘）
- GPU 100% / ~39–55 W；train-live alive
- 唯一可靠 loss 序列仍是 INFO 200–14K：0.564→0.021 后平台
- `train_config.json`：`prediction_type=epsilon`，MSE，horizon=64，DDPM 100 步，lr=1e-4，batch=8，steps=100000，cosine warmup 500

### 推导 / 结论
- DP loss 与 ACT 0.168 不同量纲，不能比大小
- 课表 W8 及格线是 100K + 真机对照表，不是某个 loss 阈值

---

## 状态快照 2026-09-15 02:05

### 观察到的事实
- train-live: step=80000, loss=0.021, last_ckpt=80000 @ 01:27:45, progress 80%, alive/healthy true
- checkpoints 现有 020000/040000/060000/080000/last
- 进程仍在：5856/5828/64204/59464；GPU 100%, 7705/8151 MiB, ~51–53 W, 53°C
- 先前「60k step 上报滞后」已由 080000 落地缓解

### 推导
- 剩余约 20000 step × 1.3 s ≈ 7.2 h；finish_at≈2026-09-15 09:18

---

## 状态快照 2026-09-15 09:36 — 训练完成

### 观察到的事实
- checkpoint **100000** 已存在，LastWriteTime=2026-09-15 08:34:20；last 同步指向该时刻
- train-live: step=100000, progress=100%, last_ckpt=100000, eta=0；updated=09:36:37
- alive=true 但 healthy=false；GPU 1% / 905 MiB / ~5.7 W（空闲）
- lerobot-train / 主训 python **已不在**；仅剩 watch-train PID 59464
- loss 字段仍为 0.021（沿用旧值，非 100K 新测）

### 推导
- W8 训练目标 steps=100000 **已达成**；进程退出 + 100k ckpt 与完成一致
- healthy=false 更可能表示「训练进程已结束」，不是中途崩溃（因 100k 已落盘）

### 假设
- 可进入评估准备：优先 EMA 权重（configs/diffusion.yaml: eval_weights=pretrained_model_ema），但 **须用户批准后** 再 load/rollout

---

## W8 EMA 评估准备 2026-09-15

### 观察到的事实
- Checkpoint: outputs/train/dp_so101_v1/checkpoints/100000/pretrained_model_ema（按 diffusion.yaml eval_weights）
- 离线/缓存修复后 DiffusionPolicy.from_pretrained → CUDA **LOAD_OK**，约 2.63e8 params；n_obs_steps=2，horizon=64
- COM3 Leader / COM4 Follower 串口在线；校准文件存在
- 相机 index 0：OpenCV 可打开 640x480 且读到帧
- 尚未执行 lerobot-rollout / 未发真机动作

### 建议 rollout（待批准）
```
call D:\SO-ARM101\activate.cmd
lerobot-rollout --strategy.type=base --policy.path=D:\SO-ARM101\outputs\train\dp_so101_v1\checkpoints\100000\pretrained_model_ema --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=150 --display_data=true
```
注意：开跑前请摆到录制起始姿态（避免折叠起步抖动 P010）；工作区清空。
