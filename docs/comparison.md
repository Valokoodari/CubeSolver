# Comparing performance

- Simple Algorithm (similar to how a beginner would solve the cube)
  - About 120 to 250 moves per solution.
  - Averages about 250 cubes per second (0.004 s / cube)
- Kociemba's Algorithm (Two-phase algorithm)
  - Almost optimal, at most 30 moves.
  - About 0 cubes per second without the pruning tables...
- Korf's Algorithm (IDA*, optimal algorithm)
  - Optimal, at most 20 moves.
  - Cubes per second? Haha, ... yeah, nope.

## Solution comparisons

### Checkerboard pattern
Scramble: `F2 B2 L2 R2 U2 D2`  

Simple algorithm:
```
Found solution: \
D D R2 F2 L2 B2 L' D' L D B' D' B D D D' R' D R F' D' F D L' D' L D D D B' D2 \
B D B' D' B D D L' D L D B D' B' D D B' D B D R D' R' D D D D2 R' D R D F D' \
F' D D2 F' D F D L D' L' D D B D' B' D' L' D L D R D' R' D' B' D B D F L D L' \
D' F' D D D R' D L D' R D L' D' D D R' D L D' R D L' D' D D D D R' D L D' R D \
L' D' D D R U R' U' R U R' U' R U R' U' R U R' U' D R U R' U' R U R' U' R U R' \
U' R U R' U' D R U R' U' R U R' U' R U R' U' R U R' U' D D \
with 185 turns in 0.004 seconds.
```
Kociemba's algorithm (no tables):
```
-- Phase 2 --
Depth:  1, checked: 10, (pruned: 0+)    
Depth:  2, checked: 77, (pruned: 33+)    
Depth:  3, checked: 533, (pruned: 247+)    
Depth:  4, checked: 3,627, (pruned: 1,713+)    
Depth:  5, checked: 24,611, (pruned: 11,669+)    
Depth:  6, checked: 37,978, (pruned: 17,855+)    

Found solution: U2 D2 L2 R2 F2 B2 with 6 turns in 4.172 seconds.
```
Korf's algorithm (no tables):
```
Depth:  1, checked: 18, (pruned: 0+)    
Depth:  2, checked: 261, (pruned: 81+)    
Depth:  3, checked: 3,501, (pruned: 1,215+)    
Depth:  4, checked: 46,755, (pruned: 16,281+)    
Depth:  5, checked: 624,123, (pruned: 217,485+)    
Depth:  6, checked: 1,505,067, (pruned: 524,442+)    

Found solution: U2 D2 L2 R2 F2 B2 with 6 turns in 332.019 seconds.
```

### Random 4 turn scramble
Scramble: `U F' R2 L'`  

Simple algorithm:
```
Found solution: \
L2 B2 F F2 F D' L D L D' B D D D R2 D D F2 D L2 B2 L' D' L D D D B' D' B D D \
R' D2 R D R' D' R D' F' D F D D L' D2 L D L' D' L D D D B' D2 B D B' D' B D F' \
D F D L D' L' B' D B D R D' R' D2 R' D R D F D' F' D D D D L D' L' D' F' D F D \
D D B D' B' D' L' D L D2 B' D B D R D' R' D F L D L' D' F' D F L D L' D' F' D \
D D D R' D L D' R D L' D' D D D D R' D L D' R D L' D' D R U R' U' R U R' U' D \
D R U R' U' R U R' U' D R U R' U' R U R' U' D \
with 181 turns in 0.008 seconds.
```
Kociemba's algorithm (no tables):
```
-- Phase 1 --
Depth:  1, checked: 18, (pruned: 0+)    
Depth:  2, checked: 261, (pruned: 81+)    
Depth:  3, checked: 770, (pruned: 261+)    

Current steps: L R2 F

-- Phase 2 --
Depth:  1, checked: 2, (pruned: 0+)    

Found solution: L R2 F U' with 4 turns in 0.090 seconds.
```
Korf's algorithm (no tables):
```
Depth:  1, checked: 18, (pruned: 0+)    
Depth:  2, checked: 261, (pruned: 81+)    
Depth:  3, checked: 3,501, (pruned: 1,215+)    
Depth:  4, checked: 10,267, (pruned: 3,564+)    

Found solution: L R2 F U' with 4 turns in 2.162 seconds.
```

### Random 5 turn scramble
Scramble: `L B2 R B' R`  

Simple algorithm:
```
Found solution: \
F2 D F B F D' L D L D' B D D D R2 D F2 L2 D B2 L' D' L D D B' D' B D D D D R' \
D' R D D D' F' D F D D' L' D L D D' B' D B R' D R D F D' F' L' D L D B D' B' D \
D D D2 R' D R D F D' F' D L D' L' D' F' D F D D D2 L' D L D B D' B' D2 B' D B \
D R D' R' F L D L' D' F' D D D L D2 L' D' L D' L' D D D R' D L D' R D L' D' R' \
D L D' R D L' D' R U R' U' R U R' U' D R U R' U' R U R' U' D R U R' U' R U R' \
U' D D \
with 165 turns in 0.008 seconds.
```
Kociemba's algorithm (no tables):
```
-- Phase 1 --
Depth:  1, checked: 18, (pruned: 0+)    
Depth:  2, checked: 261, (pruned: 81+)    
Depth:  3, checked: 3,501, (pruned: 1,215+)    
Depth:  4, checked: 46,755, (pruned: 16,281+)    
Depth:  5, checked: 392,982, (pruned: 136,941+)    

Current steps: R' B L' D2 R

-- Phase 2 --
Depth:  1, checked: 10, (pruned: 0+)    
Depth:  2, checked: 77, (pruned: 33+)    
Depth:  3, checked: 533, (pruned: 247+)    
Depth:  4, checked: 3,627, (pruned: 1,713+)    
Depth:  5, checked: 24,611, (pruned: 11,669+)    
Depth:  6, checked: 167,023, (pruned: 79,097+)    
Depth:  7, checked: 953,635, (pruned: 452,124+)    

Found solution: R' B L' D2 R F2 L2 U2 L2 F2 R2 D2 with 12 turns in 91.296 seconds.
```
Korf's algorithm (no tables):
```
Depth:  1, checked: 18, (pruned: 0+)    
Depth:  2, checked: 261, (pruned: 81+)    
Depth:  3, checked: 3,501, (pruned: 1,215+)    
Depth:  4, checked: 46,755, (pruned: 16,281+)    
Depth:  5, checked: 393,505, (pruned: 137,118+)    

Found solution: R' B R' B2 L' with 5 turns in 70.344 seconds.
```

### Random 7 turn scramble
Scramble: `B2 U' D2 B F R' F'`  

Simple algorithm:
```
Found solution: \
D F2 D D D B R D' F D L D' B D D D D R2 D D F2 D L2 B2 R' D' R D F' D' F D D D \
D B' D' B D D D D R' D' R D D D F' D' F D D D L' D2 L D L' D' L D D D B' D' B \
R' D R D F D' F' D F' D F D L D' L' D L' D L D B D' B' D D D D2 R' D R D F D' \
F' D L D' L' D' F' D F D D D2 L' D L D B D' B' D R D' R' D' B' D B D D F L D \
L' D' F' D F L D L' D' F' D D D L D2 L' D' L D' L' D D R' D L D' R D L' D' R' \
D L D' R D L' D' R U R' U' R U R' U' D D D R U R' U' R U R' U' R U R' U' R U \
R' U' D \
with 198 turns in 0.010 seconds.
```
Kociemba's algorithm (no tables):
```
-- Phase 1 --
Depth:  1, checked: 18, (pruned: 0+)    
Depth:  2, checked: 261, (pruned: 81+)    
Depth:  3, checked: 3,501, (pruned: 1,215+)    
Depth:  4, checked: 18,505, (pruned: 6,426+)    

Current steps: F R F B

-- Phase 2 --
Depth:  1, checked: 10, (pruned: 0+)    
Depth:  2, checked: 77, (pruned: 33+)    
Depth:  3, checked: 533, (pruned: 247+)    
Depth:  4, checked: 3,627, (pruned: 1,713+)    
Depth:  5, checked: 21,466, (pruned: 10,190+)    

Found solution: F R F B F2 B2 U D2 B2 with 9 turns in 2.769 seconds.
```
Korf's algorithm (no tables):
```
Depth:  1, checked: 18, (pruned: 0+)    
Depth:  2, checked: 261, (pruned: 81+)    
Depth:  3, checked: 3,501, (pruned: 1,215+)    
Depth:  4, checked: 46,755, (pruned: 16,281+)    
Depth:  5, checked: 624,123, (pruned: 217,485+)    
Depth:  6, checked: 8,331,111, (pruned: 2,903,121+)    
Depth:  7, checked: 44,050,942, (pruned: 15,350,391+)    

Found solution: F R F' B' U D2 B2 with 7 turns in 8208.674 seconds.
```
~2.25 hours

## Performance testing results for the simple algorithm
```
Solved 100000 cubes in 438.012 s.
Average time per cube: 0.004 s
Average moves per cube: 185
```
