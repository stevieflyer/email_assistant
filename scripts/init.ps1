# PowerShell script

echo "[init script] Creating in-project virtual environment..."
python -m venv ./.venv
echo "[init script] Install pip and poetry for the virtual environment..."
./.venv/Scripts/Activate.ps1
pip install --upgrade pip poetry
echo "[init script] Install dependencies..."
poetry env use ./.venv/Scripts/python.exe
poetry install
