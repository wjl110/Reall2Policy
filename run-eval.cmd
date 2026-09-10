@echo off
call D:\SO-ARM101\activate.cmd
lerobot-rollout --strategy.type=base --policy.path=outputs/train/act_so101_pick_place/checkpoints/100000/pretrained_model --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=150 --display_data=true
