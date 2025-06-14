@echo off

REM 1. Provjeri postoji li virtualno okruženje (.venv)
IF NOT EXIST ".venv\Scripts\activate.bat" (
    echo [INFO] Kreiram virtualno okruzenje .venv ...
    python -m venv .venv
)

REM 2. Aktiviraj virtualno okruzenje
call .\.venv\Scripts\activate.bat

REM Instaliraj ovisnosti
echo [INFO] Instaliram pakete iz requirements.txt ...
python.exe -m install --upgrade pip
pip install -r requirements.txt

REM Pokreni aplikaciju (trenutno train.py, kasnije možeš promijeniti u streamlit run app.py)
echo [INFO] Pokrecem treniranje modela ...
python train.py

REM Na kraju, ostavi terminal otvoren
cmd /k
