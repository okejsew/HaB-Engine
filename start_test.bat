@echo off
chcp 65001 >nul
python test.py 1>nul
if %errorlevel% neq 0 (
    echo.
)
pause