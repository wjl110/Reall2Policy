"""Merge 100 expert episodes + dagger3 (intervention column dropped) for ACT-v3."""

from pathlib import Path

from lerobot.datasets.dataset_tools import merge_datasets, remove_feature
from lerobot.datasets.lerobot_dataset import LeRobotDataset

ROOT = Path(r"D:\SO-ARM101\data\local")
EXPERT = ROOT / "so101_pick_place_20260910_011033"
DAGGER3 = ROOT / "rollout_so101_dagger3"
PLAIN = ROOT / "rollout_so101_dagger3_plain"
MIX = ROOT / "so101_v3_mix"


def main() -> None:
    if not PLAIN.joinpath("meta", "info.json").is_file():
        print("Removing intervention from dagger3 ->", PLAIN)
        src = LeRobotDataset("local/rollout_so101_dagger3", root=DAGGER3)
        remove_feature(
            src,
            feature_names=["intervention"],
            output_dir=PLAIN,
            repo_id="local/rollout_so101_dagger3_plain",
        )
    else:
        print("Reuse existing", PLAIN)

    print("Merging expert + plain dagger3 ->", MIX)
    expert = LeRobotDataset("local/so101_pick_place", root=EXPERT)
    plain = LeRobotDataset("local/rollout_so101_dagger3_plain", root=PLAIN)
    merged = merge_datasets(
        [expert, plain],
        output_repo_id="local/so101_v3_mix",
        output_dir=MIX,
    )
    print(
        f"OK episodes={merged.meta.total_episodes} frames={merged.meta.total_frames}"
    )


if __name__ == "__main__":
    main()
