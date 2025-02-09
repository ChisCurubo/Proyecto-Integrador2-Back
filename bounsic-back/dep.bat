pip freeze > requirements.txt
pip install -r requirements.txt

# para pycache 
python -m compileall .

set PYTHONPYCACHEPREFIX=.\pycache
