@echo off
cd /d %~dp0
echo Iniciando servidor FastAPI...
pip install -r requirements.txt
set PYTHONPYCACHEPREFIX=.\pycache
set PYTHONPATH=%CD%
python app/server.py
pause
