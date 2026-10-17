@echo off
chcp 65001 > nul
cd /d "%~dp0"
python build_battery3.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Pipeline execution failed.
    exit /b %ERRORLEVEL%
)
echo [SUCCESS] Battery 3 Dashboard and Master Report generated successfully.
