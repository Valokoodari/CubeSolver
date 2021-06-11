if [ -d "venv" ]
then    # Activate the virtual environment
    . venv/bin/activate
else    # Set up the virtual environment if it doesn't exist already
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
fi

mkdir ./tmp

pylint src --output-format=text | tee ./tmp/pylint.log || pylint-exit $?
PYLINT_SCORE=$(sed -n 's/^Your code has been rated at \([-0-9.]*\)\/.*/\1/p' ./tmp/pylint.log)
anybadge -l pylint -v $PYLINT_SCORE -o -f ./.github/badges/pylint.svg 0=black 1=maroon 3=red 5=orange 7=yellow 8=yellowgreen 9=green 10=lime

rm -r tmp
