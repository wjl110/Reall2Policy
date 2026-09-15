@echo off
cd /d D:\SO-ARM101
call D:\SO-ARM101\activate.cmd
lerobot-rollout --strategy.type=base --policy.path=D:\SO-ARM101\outputs\train\dp_so101_v1\checkpoints\100000\pretrained_model_ema --robot.type=so101_follower --robot.port=COM4 --robot.id=so101_follower --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}}" --task="Pick up the object and place it down." --duration=900 --display_data=true --play_sounds=false
