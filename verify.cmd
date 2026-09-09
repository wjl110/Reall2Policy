@echo off
call "%~dp0activate.cmd"
python "%~dp0verify.py"
if errorlevel 1 exit /b 1
python -m pip check
