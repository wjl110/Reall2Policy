# Real2Policy 12 周课表（本机命令）

固定：双击 `start.cmd` 再贴命令。Leader=`COM3` / Follower=`COM4`。不上 Hub。
带相机的 record / teleoperate / rollout **一律** `--display_data=true`（Rerun 实时画面；本机 OpenCV headless，没有 cv2 窗口）。
训练窗口占用 GPU 时，**不要**在同一窗口录数据；也不要 `resume` 正在被训练读的那个数据集。

| 周 | 状态 | 产物 |
|---|---|---|
| W0 环境 | 完成 | `env/` + `verify.cmd` |
| W1 遥操 | 完成 | 校准 + teleop |
| W2 数据 | **完成 100/100** | `so101_pick_place_20260910_011033` |
| W3 ACT | **E01/E02/E03 完成 100K** | E03 loss 0.168 @100K |
| W4 拔 Leader | **完成** | `assets/demo.mp4` |
| W5–6 Eval/OOD | **完成** | Cam 19/90；Pos/Obj 0/90 |
| W7 Flywheel | **评测齐** | v3 IID 8/90；Pos **13/90**（E03 Pos 0） |
| W8 ACT vs DP | **进行中** | DP **100K 已齐**；待真机 |
| W9–W12 | 未开始 | — |

任务只做一件：`Pick up the object and place it down.`（Random-position Pick & Place）

---

## 现在立刻

W8：Diffusion **100K 已齐**（`outputs/train/dp_so101_v1/checkpoints/100000` @08:34）。100K loss 无日志，不编造。日常仍用 E03。不要开 VLA。

先 IID，必须先摆到录制起始姿态。用 **EMA** 权重：

```bat
lerobot-rollout --strategy.type=base --policy.path=outputs/train/dp_so101_v1/checkpoints/100000/pretrained_model_ema --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=60 --display_data=true
```


---

## Week 0（已完成，复检）

```bat
verify.cmd
lerobot-find-port
```

---

## Week 1（已完成，复检）

```bat
lerobot-calibrate --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower
lerobot-calibrate --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader
```

```bat
lerobot-teleoperate --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --display_data=true
```

夹爪过载：松爪，等灯灭再开。

---

## Week 2：补到 100 episodes

现有 20 条。`resume` 时 `--dataset.num_episodes` = **本次数**，不是总数。

覆盖（每格至少 8–10 条）：Left / Center / Right / Near / Far；正常光 + 略变光；Approach A/B/C。失败按 `r`。

**+30 → 共 50（E02 用）：**

```bat
lerobot-record --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.num_episodes=30 --dataset.episode_time_s=20 --dataset.reset_time_s=8 --dataset.single_task="Pick up the object and place it down." --dataset.push_to_hub=false --resume=true --display_data=true
```

**再 +50 → 共 100（E03 用）：** 同上，只改 `--dataset.num_episodes=50`。

回放抽检：

```bat
lerobot-replay --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.episode=0
```

分析 notebook：

```bat
jupyter notebook experiments\E002\dataset_analysis.ipynb
```

（文件在补采后建。先看 `data\local\so101_pick_place_20260910_011033\meta\info.json` 的 `total_episodes`。）

---

## Week 3：ACT（先这一条，不要并行 DP/VLA）

| Exp | Episodes | 数据 | 输出 |
|---|---:|---|---|
| E01 | 20 | 当前这份 | `outputs/train/act_so101_pick_place`（**100K 完成**） |
| E02 | 50 | 同 root 补到 50 后 | `outputs/train/act_so101_e02`（**100K 完成**） |
| E03 | 100 | 同 root 已 100 | `outputs/train/act_so101_e03`（**100K 完成**，loss 0.168） |

E01 勿重开同目录。E02（50 条已齐，现在跑）：

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=act --output_dir=outputs/train/act_so101_e02 --job_name=act_so101_e02 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=8 --steps=100000
```

E03：`--output_dir=outputs/train/act_so101_e03 --job_name=act_so101_e03`。

结果记到 `experiments/INDEX.md`。

---

## Week 4：拔掉 Leader（Milestone 1）

用当前最好 ckpt（E03 的 `100000`）：

```bat
lerobot-rollout --strategy.type=base --policy.path=outputs/train/act_so101_e03/checkpoints/100000/pretrained_model --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=60 --display_data=true
```

必须先摆到录制起始姿态。录 30–60s Demo → `assets/demo.mp4`。

---

## Week 5–6：Evaluation + OOD

每种条件 **30–50** 次，填 `results/eval_w56.md`（先复制 `results/eval_template.md`）。

条件：IID / Position OOD / Object OOD / Lighting OOD / Background OOD / Camera Shift。

失败归类：Perception / Approach / Grasp / Transport / Placement / Timeout。

命令与 W4 相同，改桌面布置，每次记成功/失败。

---

## Week 7：Data Flywheel

针对 W6 最差条件加采。**优先 DAgger / HITL**（policy 自己跑 → 快失败时人接管 → 纠正后交回 → 整段保存）。不要 resume 现有 100 ep（schema 多 `intervention`，且 rollout 数据集名必须 `rollout_`）。插回 Leader。Space=暂停/恢复，Tab=开始/结束纠正。

```bat
lerobot-rollout --strategy.type=dagger --strategy.record_autonomous=true --strategy.num_episodes=50 --policy.path=outputs/train/act_so101_e03/checkpoints/100000/pretrained_model --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --dataset.repo_id=local/rollout_so101_dagger --dataset.root=D:\SO-ARM101\data\local\rollout_so101_dagger --dataset.single_task="Pick up the object and place it down." --dataset.push_to_hub=false --display_data=true
```

纯遥操补采（备选，不要和 DAgger 并行开）：

```bat
lerobot-record --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.num_episodes=50 --dataset.episode_time_s=20 --dataset.reset_time_s=8 --dataset.single_task="Pick up the object and place it down." --dataset.push_to_hub=false --resume=true --display_data=true
```

然后 ACT-v2：

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=act --output_dir=outputs/train/act_so101_v2 --job_name=act_so101_v2 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=8 --steps=100000
```

复测 W6 表，对比 ACT-v1 → v2。

---

## Week 8：ACT vs Diffusion（同一 Dataset）

本机先装依赖（只需一次）：

```bat
pip install -e .\lerobot[diffusion]
```

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=diffusion --ema.enable=true --output_dir=outputs/train/dp_so101_v1 --job_name=dp_so101_v1 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=8 --steps=100000 --accelerator.mixed_precision=bf16
```

```bat
lerobot-rollout --strategy.type=base --policy.path=outputs/train/dp_so101_v1/checkpoints/100000/pretrained_model_ema --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=60 --display_data=true
```

比：IID / OOD / 训练时间 / 推理延迟 / Grasp fail / Place fail。填 `results/act_vs_dp.md`。

---

## Week 9–10：SmolVLA

官方微调 `lerobot/smolvla_base`，不要从零。数据必须是下面的语言指令集，不要用 100 ep 抓放集、不要混 Hub 集。W7/W8 未完、GPU 被占时不要跑。

```bat
pip install -e ".\lerobot[smolvla]"
```

新开 `local/so101_lang`。每条指令一批，只改 `single_task`。第一批不要 `--resume`；后两批加 `--resume=true`。

```text
Pick up the red block.
Put the block into the box.
Move the blue object to the left.
```

第一批（约 20 条）：

```bat
lerobot-record --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --dataset.repo_id=local/so101_lang --dataset.root=D:\SO-ARM101\data\local\so101_lang --dataset.num_episodes=20 --dataset.episode_time_s=20 --dataset.reset_time_s=8 --dataset.single_task="Pick up the red block." --dataset.push_to_hub=false --display_data=true
```

后两批：同上，加 `--resume=true`，`single_task` 换成另外两句。

```bat
lerobot-train --policy.path=lerobot/smolvla_base --dataset.repo_id=local/so101_lang --dataset.root=D:\SO-ARM101\data\local\so101_lang --dataset.video_backend=pyav --output_dir=outputs/train/smolvla_so101_v1 --job_name=smolvla_so101_v1 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=4 --steps=20000
```

若报相机数不够（base 常见双机位，本机只有 `front`），在训练命令末尾加 `--policy.empty_cameras=1`。

```bat
lerobot-rollout --strategy.type=base --policy.path=outputs/train/smolvla_so101_v1/checkpoints/020000/pretrained_model --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the red block." --duration=60 --display_data=true
```

显存不够再降 `batch_size` 或租 GPU。

---

## Week 11：World Model 延伸

用已有 `(o_t, a_t, o_{t+1})` 做预测实验。命令与 notebook 到该周再写，本周不要提前做。

---

## Week 12：作品集

```bat
gh auth login
gh repo create Reall2Policy --public --source=. --remote=origin
git push -u origin HEAD
```

HF（数字齐了再传）：

```bat
huggingface-cli login
```

Demo 结构：10s 问题 → 20s 采集 → 20s 训练 → 30s 真机 → 30s OOD → 10s 数字。

---

## 每周节奏

| 日 | 做什么 |
|---|---|
| 一、二 | 工程：环境 / 数据 / 机器人 |
| 三、四 | 算法：训练 / 实验 |
| 五 | 轻量：记 `experiments/`、README |
| 六、日 | 大实验：采集 / eval / 训练 / 拍 Demo |

精力：Data 30% / Policy 25% / Eval 20% / Eng 15% / Docs 10%。
