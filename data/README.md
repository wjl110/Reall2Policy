# Data

本地 LeRobot 数据集。不上 Hub，除非 Week 12 明确要推。

当前训练数据：

```
data/local/so101_pick_place_20260910_011033
```

- repo_id: `local/so101_pick_place`
- 任务: Pick up the object and place it down.
- 相机: front 640×480 @ 30

2026-09-10 已清理试录、空壳、中断目录。补采时必须带 `--dataset.root` 指向上述目录，不要另开新文件夹。
