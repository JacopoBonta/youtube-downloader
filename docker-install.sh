#!/bin/bash
if [ -f requirements.txt ]; then
    echo "requirements.txt found. Installing requirements..."
    pip3 install -r requirements.txt
fi

echo "Done"