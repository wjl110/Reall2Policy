@echo off
call "%~dp0activate.cmd"
python "%~dp0scripts\watch-train.py" --job dp_so101_v1 --interval 2 --open
