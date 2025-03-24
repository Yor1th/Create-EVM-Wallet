@echo off
echo Установка необходимых библиотек...
pip install mnemonic pandas eth_account
pip install pyfiglet
echo Запуск wall.py...
python wall.py
pause
