# CubeSolver  

[![Python application](https://github.com/Valokoodari/CubeSolver/actions/workflows/python-app.yml/badge.svg)](https://github.com/Valokoodari/CubeSolver/actions/workflows/python-app.yml)
[![codecov](https://codecov.io/gh/Valokoodari/CubeSolver/branch/main/graph/badge.svg?token=YK2TYFN4JL)](https://codecov.io/gh/Valokoodari/CubeSolver)
![pylint](.github/badges/pylint.svg)

A Python program to compare Kociemba's algorithm, Korf's algorithm, and a basic 
way to solve a Rubik's cube. The basic solve should be the fastest but the 
solution could have hundreds of turns while Kociemba's and Korf's algorithms 
should find a solution which is at least close to the optimal solution.  

Any valid state of the 3x3x3 Rubik's cube is at most 20 moves away from the 
solved state.

## Documentation  
- [Project Specification](docs/specification.md)  
- [Implementation document](docs/implementation.md)  
- [Testing document](docs/testing.md)  
- [User guide](docs/guide.md)  

### Weekly reports  
- [Week 1](docs/week_1.md)  
- [Week 2](docs/week_2.md)  
- [Week 3](docs/week_3.md)  
- [Week 4](docs/week_4.md)  
- [Week 5](docs/week_5.md)  
- [Week 6](docs/week_6.md)  

### Run the program
```
./run.sh
```

### Run tests and check style
```
./test.sh
```  

### Build the program for the current OS
```
./build.sh
```
