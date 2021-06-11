if [ -d "venv" ]
then    # Activate the virtual environment
    . venv/bin/activate
else    # Set up the virtual environment if it doesn't exist already
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
fi

# Create a folder for temporary files
mkdir tmp

# Check the code for style errors with flake8
echo "Syntax error and undefined names:"
flake8 . --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
echo
echo "Code style errors:"
flake8 . --exclude=venv --count --exit-zero --max-complexity=10 --max-line-length=80 --statistics

# Check the code for style errors with pylint and create a badge
echo
echo "Pylint scoring:"
pylint src test --output-format=text | tee ./tmp/pylint.log || pylint-exit $?
PYLINT_SCORE=$(sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' ./tmp/pylint.log)
anybadge -l pylint -v $PYLINT_SCORE -o -f ./.github/badges/pylint.svg 2=black 4=maroon 5=red 6=orange 7=yellow 8=yellowgreen 9=green 10=lime

# Run tests
echo
pytest -v --cov=src

# Clean up
rm -r tmp
