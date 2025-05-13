@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

where python >nul 2>nul
if %errorlevel% NEQ 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b
)

echo Checking Microsoft Word availability...
python -c "import win32com.client; win32com.client.Dispatch('Word.Application')" >nul 2>nul
if %errorlevel% NEQ 0 (
    echo [ERROR] Microsoft Word is not installed or cannot be accessed via COM.
    pause
    exit /b
)

echo Installing Python dependencies...
pip install -r requirements.txt >nul
if %errorlevel% NEQ 0 (
    echo [ERROR] Failed to install dependencies.
    pause
    exit /b
)

start "" cmd /c start_servers.bat

timeout /t 3 /nobreak >nul
start http://localhost:8000

exit
