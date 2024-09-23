# /usr/bin/env bash

echo "[init script] Creating in-project virtual environment..."
python -m venv ./.venv
echo "[init script] Install pip and poetry for the virtual environment..."
source ./.venv/bin/activate
pip install --upgrade pip poetry
echo "[init script] Install dependencies..."
poetry env use ./.venv/bin/python
poetry install
