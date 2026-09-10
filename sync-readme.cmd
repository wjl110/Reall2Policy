@echo off
call "%~dp0activate.cmd"
python "%~dp0scripts\sync-readme.py"
exit /b %ERRORLEVEL%
