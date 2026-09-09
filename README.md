# Real2Policy

End-to-end real-world robot learning on LeRobot SO-101.

`20 demonstrations (target 100) · ACT (training) · Diffusion Policy · SmolVLA · OOD Generalization`

> 数字以 `experiments/INDEX.md` 与 `results/` 为准，未测完不写成功率。

## Demo

（Week 4 后放 `assets/demo.mp4`）

## 当前进度

课表与全部可复制命令：**[docs/COURSE.md](docs/COURSE.md)**

| 周 | 状态 |
|---|---|
| W0 环境 / W1 遥操 | 完成 |
| W2 Dataset | 20/100 episodes |
| W3 ACT | 进行中 |
| W4–W12 | 未开始 |

Architecture → Results → Benchmark → Failure Analysis → Reproduction：随周次补齐。

## 本机启动

1. 双击 `start.cmd`
2. `verify.cmd`
3. 按 [docs/COURSE.md](docs/COURSE.md) 执行当周命令

Windows 环境细节见 [使用说明.md](使用说明.md)。实验台账：`lab-log/`。

## 仓库

```
configs/     act / diffusion / smolvla
data/        本地 demonstration（不上 Hub）
docs/        课表与方法
experiments/ E01–E08
results/     eval / ACT vs DP
assets/      Demo
scripts/     评测与部署（W4 起）
```

`env/`、`cache/`、`outputs/` 不进 Git。

## 许可证

`lerobot/` 为 Apache 2.0。其余项目文件同样 Apache 2.0。
