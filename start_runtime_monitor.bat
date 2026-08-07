@echo off
title Runtime Monitor

cd /d D:\IEInfoSvcs\runtime-monitor

echo ==========================================
echo Starting Runtime Monitor
echo Directory: %CD%
echo Date: %DATE%
echo Time: %TIME%
echo ==========================================
echo.

"C:\Users\barbl\AppData\Local\Programs\Python\Python311\python.exe" main.py

echo.
echo Runtime Monitor exited.
pause