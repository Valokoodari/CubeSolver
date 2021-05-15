# CubeSolver  

[![Python application](https://github.com/Valokoodari/CubeSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/Valokoodari/CubeSolver/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/Valokoodari/CubeSolver/branch/main/graph/badge.svg?token=YK2TYFN4JL)](https://codecov.io/gh/Valokoodari/CubeSolver)

A Python program to compare a couple of different ways to find a solution for a 
Rubik's cube.  

## Documentation  
- [Project Specification](docs/specification.md)  

### Weekly reports  
- [Week 1](docs/week_1.md)  

### Run Tests  
```
pytest -v --cov-report term --cov=src
```  

### Check Code Style  
```
flake8 . --exclude=venv --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --exclude=venv --count --exit-zero --max-complexity=10 --max-line-length=80 --statistics
```  