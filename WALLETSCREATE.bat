@echo off
cd %USERPROFILE%\Desktop\12345
echo Установка необходимых библиотек...
pip install mnemonic pandas eth_account
echo Запуск wall.py...
python wall.py
pause
