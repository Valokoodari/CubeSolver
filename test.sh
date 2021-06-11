if [ -d "venv" ]
then    # Activate the virtual environment
    . venv/bin/activate
else    # Set up the virtual environment if it doesn't exist already
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
fi

# Check the code for style errors with flake8
echo "Syntax error and undefined names:"
flake8 . --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
echo
echo "Code style errors:"
flake8 . --exclude=venv --count --exit-zero --max-complexity=10 --max-line-length=80 --statistics

# Check the code for style errors with pylint
echo
echo "Pylint scoring:"
pylint src

# Run tests
echo
pytest -v --cov=src
