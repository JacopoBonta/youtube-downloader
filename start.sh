if [ ! -d .venv/ ]; then
    echo "virtual environment not found"
    exit 1
fi

source .venv/bin/activate

python3 main.py