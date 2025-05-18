#!/bin/bash

echo "Activare venv:"

# Încearcă multiple locații posibile pentru venv
if [ -f ".venv/bin/activate" ]; then
    echo "Activez venv local (.venv)..."
    . ./.venv/bin/activate
elif [ -f "../.venv/bin/activate" ]; then
    echo "Activez venv din directorul părinte..."
    . ../.venv/bin/activate
elif [ -f "/home/cxb/proiect_scc/curs_vcgj_4_tari/venv/bin/activate" ]; then
    echo "Activez venv din calea hardcodată..."
    . /home/cxb/proiect_scc/curs_vcgj_4_tari/venv/bin/activate
else
    echo "EROARE: Nu s-a găsit niciun venv pentru activare!"
    echo "Creez un venv nou..."
    python3 -m venv .venv
    . ./.venv/bin/activate
    pip install -r requirements.txt
fi

# Verifică dacă venv-ul a fost activat corect
if [ -n "$VIRTUAL_ENV" ]; then
    echo "Venv activat cu succes: $VIRTUAL_ENV"
else
    echo "EROARE: Activarea venv a eșuat!"
    exit 1
fi

echo "Configurare variabilă mediu FLASK_APP"
export FLASK_APP=tari
export PYTHONPATH=.

# Afișează informații despre directorul curent
CALE=$(pwd)
echo "CALE: $CALE"
echo "CONTINUT DIRECTOR:"
ls -la

echo "Start server:"
# Folosește exec pentru a înlocui procesul curent cu serverul Flask
exec flask run -h 0.0.0.0 -p 5011 --reload