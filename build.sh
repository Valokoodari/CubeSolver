if [ -d "venv" ]
then    # Activate the virtual environment
    . venv/bin/activate
else    # Set up the virtual environment if it doesn't exist already
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
fi

# Build the program for the current OS.
pyinstaller --onefile src/cubesolver.py

# Clean up after the build
rm -r build
