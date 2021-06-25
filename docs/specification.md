# Project Specification  
### Tietojenkäsittelytieteen kandidaatti (TKT), Project language: english  

This program is for comparing a few different ways to find a solution for a 
Rubik's cube. The comparison includes the time to find a solution and the
amount of turns in the solution. The program is written in Python.

## Data structures  
- Cube (3x3x3)
  - 6 x CubeFace (3x3)
    - Stored as a 32-bit integer and manipulated with bitwise operations.
- Pruning tables
  - Lists of ints (-1..20) used to store the minimum required moves for the 
    given index (coordinate or state of the cube).

## Algorithms  
- My own algorithm based somewhat on how I solve a cube  
  - Solves the cube layer by layer
  - A lot of moves
- **Kociemba's algorithm** (two-phase algorithm)  
  - Solves the Cube in two phases:
    - **Phase 1** in which every face rotation of the Cube is allowed. (18 
      different face rotations which are explained
      [here](https://ruwix.com/the-rubiks-cube/notation/)) The goal of this 
      phase is to reach a state where the cube is valid for the phase 2 or a 
      solved cube. This phase will take at most 12 face rotations.  
    - **Phase 2** in which only the face rotations possible on a Domino cube 
      (U, U2, U', D, D2, D', R2, L2, F2, and B2) are allowed. This phase will 
      take at most 18 face rotations.  
- **Korf's algorithm** (IDA*)  
  - Solves the cube in just one phase with all of the face rotations always 
    available. Uses three different patterns from the cube as coordinates to 
    estimate the minimum moves required (corners, first six edges, last 6
    edges).  

## Expected time and space complexity
- Unknown

## Input / Output  
### Input  
- The state of the puzzle or a random scramble.  
  - Random scramble always has 20 rotations (18 in group G1) but the rotations
    can cancel each other out completely or partially.  
  - A state can be given in the basic notation (=face rotations only).

### Output  
- The lists of moves to solve the cube for each algorithm.

## Sources  
- [Herbert Kociemba, The Two-Phase algorithm](http://www.kociemba.org/cube.htm)  
- [Richard E. Korf, Finding Optimal Solutions to Rubik's Cube Using Pattern Databases](https://www.cs.princeton.edu/courses/archive/fall06/cos402/papers/korfrubik.pdf)  