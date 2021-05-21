# Create the virtual environment if it doesn't exist already
if [ ! -d "venv" ]
then
    python3 -m venv venv
    pip -r requirements.txt
fi

# Activate the virtual environment
source venv/bin/activate

# Check the code for style errors
echo "Syntax error and undefined names:"
flake8 . --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
echo "\nCode style errors:"
flake8 . --exclude=venv --count --exit-zero --max-complexity=10 --max-line-length=80 --statistics

echo ""
# Run tests
pytest -v --cov-report term --cov=src
