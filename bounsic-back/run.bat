@echo off
echo Iniciando Bounsic Backend...
cd /d %~dp0
call venv\Scripts\activate
pip install -r requirements.txt
set PYTHONPYCACHEPREFIX=.\pycache
set FLASK_ENV=development   
python app/server.py
pause
