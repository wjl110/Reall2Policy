# Real2Policy 12 周课表（本机命令）

固定：双击 `start.cmd` 再贴命令。Leader=`COM3` / Follower=`COM4`。不上 Hub。
训练窗口占用 GPU 时，**不要**在同一窗口录数据；也不要 `resume` 正在被训练读的那个数据集。

| 周 | 状态 | 产物 |
|---|---|---|
| W0 环境 | 完成 | `env/` + `verify.cmd` |
| W1 遥操 | 完成 | 校准 + teleop |
| W2 数据 | **进行中 20/100** | `so101_pick_place_20260910_011033` |
| W3 ACT | **进行中 ~40K/100K** | `outputs/train/act_so101_pick_place` |
| W4–W12 | 未开始 | — |

任务只做一件：`Pick up the object and place it down.`（Random-position Pick & Place）

---

## 现在立刻

训练接着跑，别停。看 step / loss：

```bat
findstr /C:"step:" C:\Users\18431\.cursor\projects\d-SO-ARM101\terminals\6.txt
```

若中断，续训：

```bat
lerobot-train --config_path=outputs/train/act_so101_pick_place/checkpoints/020000/pretrained_model/train_config.json --resume=true
```

训练结束后才做 W2 补采。

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
lerobot-teleoperate --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --display_data=true
```

夹爪过载：松爪，等灯灭再开。

---

## Week 2：补到 100 episodes

现有 20 条。`resume` 时 `--dataset.num_episodes` = **本次数**，不是总数。

覆盖（每格至少 8–10 条）：Left / Center / Right / Near / Far；正常光 + 略变光；Approach A/B/C。失败按 `r`。

**+30 → 共 50（E02 用）：**

```bat
lerobot-record --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.num_episodes=30 --dataset.episode_time_s=20 --dataset.reset_time_s=8 --dataset.single_task="Pick up the object and place it down." --dataset.push_to_hub=false --resume=true
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
| E01 | 20 | 当前这份 | `outputs/train/act_so101_pick_place`（在跑） |
| E02 | 50 | 同 root 补到 50 后 | `outputs/train/act_so101_e02` |
| E03 | 100 | 同 root 补到 100 后 | `outputs/train/act_so101_e03` |

E01 已启动，勿重开同目录。E02 示例（50 条齐了再跑）：

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=act --output_dir=outputs/train/act_so101_e02 --job_name=act_so101_e02 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=8 --steps=100000
```

E03：`--output_dir=outputs/train/act_so101_e03 --job_name=act_so101_e03`。

结果记到 `experiments/INDEX.md`。

---

## Week 4：拔掉 Leader（Milestone 1）

用当前最好 ckpt（先 E01 的 `020000` 或训完后的最后一档）：

```bat
lerobot-rollout --strategy.type=base --policy.path=outputs/train/act_so101_pick_place/checkpoints/020000/pretrained_model --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=60 --display_data=true
```

训完 100K 后把 `020000` 换成最大数字目录。录 30–60s Demo → `assets/demo.mp4`。

---

## Week 5–6：Evaluation + OOD

每种条件 **30–50** 次，填 `results/eval_w56.md`（先复制 `results/eval_template.md`）。

条件：IID / Position OOD / Object OOD / Lighting OOD / Background OOD / Camera Shift。

失败归类：Perception / Approach / Grasp / Transport / Placement / Timeout。

命令与 W4 相同，改桌面布置，每次记成功/失败。

---

## Week 7：Data Flywheel

针对 W6 最差条件加采 hard cases（例 +50）：

```bat
lerobot-record --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --teleop.type=so101_leader --teleop.port=COM3 --teleop.id=so101_leader --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.num_episodes=50 --dataset.episode_time_s=20 --dataset.reset_time_s=8 --dataset.single_task="Pick up the object and place it down." --dataset.push_to_hub=false --resume=true
```

然后 ACT-v2：

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=act --output_dir=outputs/train/act_so101_v2 --job_name=act_so101_v2 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=8 --steps=100000
```

复测 W6 表，对比 ACT-v1 → v2。

---

## Week 8：ACT vs Diffusion（同一 Dataset）

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=diffusion --ema.enable=true --output_dir=outputs/train/dp_so101_v1 --job_name=dp_so101_v1 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=8 --steps=100000
```

```bat
lerobot-rollout --strategy.type=base --policy.path=outputs/train/dp_so101_v1/checkpoints/100000/pretrained_model_ema --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=60 --display_data=true
```

比：IID / OOD / 训练时间 / 推理延迟 / Grasp fail / Place fail。填 `results/act_vs_dp.md`。

---

## Week 9–10：SmolVLA

```bat
pip install -e ".\lerobot[smolvla]"
```

语言指令录制（每条指令各一批，`single_task` 换成对应英文）：

```text
Pick up the red block.
Put the block into the box.
Move the blue object to the left.
```

```bat
lerobot-train --dataset.repo_id=local/so101_pick_place --dataset.root=D:\SO-ARM101\data\local\so101_pick_place_20260910_011033 --dataset.video_backend=pyav --policy.type=smolvla --output_dir=outputs/train/smolvla_so101_v1 --job_name=smolvla_so101_v1 --policy.device=cuda --wandb.enable=false --policy.push_to_hub=false --batch_size=4 --steps=20000
```

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
