import importlib
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
report = {"python": sys.version, "executable": sys.executable, "versions": {}}
for package in ["lerobot", "torch", "torchvision", "torchcodec", "av", "numpy", "opencv-python-headless", "feetech-servo-sdk"]:
    report["versions"][package] = importlib.metadata.version(package)
for module in ["cv2", "av", "serial", "scservo_sdk", "datasets", "accelerate", "lerobot.robots.so_follower", "lerobot.teleoperators.so_leader", "lerobot.policies.act.modeling_act", "lerobot.datasets.lerobot_dataset"]:
    importlib.import_module(module)

from lerobot.robots.config import RobotConfig
from lerobot.teleoperators.config import TeleoperatorConfig

assert RobotConfig.get_choice_class("so101_follower")
assert TeleoperatorConfig.get_choice_class("so101_leader")
report["so101"] = "leader/follower implementations imported and CLI registry checked"

import torch
import torchvision
from torchcodec.decoders import VideoDecoder

assert torch.cuda.is_available(), "CUDA is unavailable"
matrix = torch.randn(256, 256, device="cuda")
result = matrix @ matrix.T
torch.cuda.synchronize()
assert torch.isfinite(result).all().item()
report["gpu"] = {"name": torch.cuda.get_device_name(0), "cuda": torch.version.cuda, "capability": torch.cuda.get_device_capability(0), "matrix_test": "passed"}
video = root / "logs" / "verification-video.mp4"
subprocess.run(["ffmpeg", "-y", "-f", "lavfi", "-i", "testsrc=size=64x64:rate=5", "-t", "1", "-c:v", "libsvtav1", "-pix_fmt", "yuv420p", str(video)], check=True, capture_output=True)
decoder = VideoDecoder(str(video), device="cpu")
assert decoder[0].shape == (3, 64, 64)
report["video"] = "FFmpeg libsvtav1 encode + TorchCodec decode passed"
report["cli"] = {}
for command in ["lerobot-teleoperate", "lerobot-record", "lerobot-calibrate", "lerobot-train"]:
    completed = subprocess.run([command, "--help"], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=90)
    (root / "logs" / f"{command}-help.txt").write_text(completed.stdout + completed.stderr, encoding="utf-8")
    assert completed.returncode == 0, f"{command} failed: {completed.stderr[-2000:]}"
    report["cli"][command] = "passed"
report["hardware"] = "Not connected or commanded; motor and camera hardware unverified"
(root / "logs" / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
