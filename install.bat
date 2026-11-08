@echo off
setlocal
cd /d "%~dp0"
echo Installing Thaara AI 2.1 (one-time setup)...
py -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if not exist .env copy .env.example .env
echo.
echo Setup complete. Edit .env if you want API keys.
echo Start with: run_thaara.bat
pause
