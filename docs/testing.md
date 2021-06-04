# Testing

## Unit tests
- Coordinates used to identify different cube states are tested with a few
  manually calculated situations selected at random.  

(The only true unit tests are for the class CubeFace)

## Integration tests
The program structure is quite linear so every layer also tests the layers 
which it depends on.

For example:  
Kociemba > Cube > CubeFace  
(Kociemba requires Cube and Cube requires CubeFace)  

## Random input
Some tests have input randomized every time the tests are run. These tests are 
intended to help find bugs which may occur with just a few different states of 
the cube.  

## Help with testing

### Run all tests
```
./test.sh
```

### Run test from specific file
```
pytest -s -q <file>
```
(e.g. `pytest -s -q test/puzzle/test_cube.py`)

### Run a single test
```
pytest -k <test_name>
```
(e.g. `pytest -k test_checkerboard_is_domino`)