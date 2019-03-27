#!/bin/bash
if [ ! -d .venv/ ]; then
    python3 -m venv .venv
    echo "new virtual environment created in .venv/"
fi

source .venv/bin/activate

if [ -f requirements.txt ]; then
    echo "requirements.txt found. Installing requirements..."
    pip install -r requirements.txt
fi

echo "Done"