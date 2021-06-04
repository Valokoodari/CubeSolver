# Weekly report 4  

## What did I do this week?  
| Date  | Time (h) | Task
| :---: | :---     | :---
| 1.6.  | 0.5      | Improved duplicate check prevention for Kociemba's. (Prevent checking of ```U D U'``` (same as just ```D```) and ```R' L2 R2``` (same as ```R L2```) for example.)
|       | 1.5      | Functions for Kociemba's coordinates for pruning.
|       | 1        | Reading and trying to understand the coordinates.
|       | 1        | Writing tests and manual testing.
| 2.6.  | 0.5      | This table to replace the old list.
|       | 0.5      | Even better duplicate prevention. (For example: only check ```L R``` or ```R L```, never both.)
|       | 0.5      | Remember cubes which have already been checked.
|       | 0.5      | Combine Kociemba's __phase1 and __phase2 to only be one function __search with different check function and moveset.
|       | 0.5      | Style fixes and manual testing.
|       | 1        | Fixed this on Linux as apparently this did only work on macOS.
| 3.6.  | 1        | Calculation of the corner permutation coordinate.
| 4.6.  | 2.5      | Manual testing and fixing bugs
|       | 2        | Calculation of the edge permutation coordinate.
|       | 0.5      | Building of an executable on macOS and Linux
|       | 0.5      | Documentation: testing, implementation, guide.
|       | 0.5      | Calculation of the UD slice phase 2 coordinate.
|       | 0.5      | Calculation of the UD slice coordinate.
|       | 0.5      | Calculation of the edge orientation coordinate.
|       | 0.5      | Calculation of the corner orientation coordinate.
| Total | 16       |

## Progress on the program  
- Calculation of all of the coordinates for Kociemba's algorithm. (Ready for
  pruning, yay!)  

## What did I learn?  
- This course with this problem was a really bad idea when I also have the
  software engineering lab at the same time. (I'm still not giving up though)  
- Implementing multithreading with Python is suprisingly hard and I probably
  don't have enough time to think about it.  

## Challenges?  
- Python is quite slow :) I should have gone with C++ or Rust instead.  
- There is a weird bug and some orientations are not checked:
```
-- Phase 2 --
Depth:  1, checked: 10
Depth:  2, checked: 77
Depth:  3, checked: 533
Depth:  4, checked: 3592
Depth:  5, checked: 20231
Depth:  6, checked: 57528
Depth:  7, checked: 131706
Depth:  8, checked: 379979
Depth:  9, checked: 473862
Depth: 10, checked: 1022341
Depth: 11, checked: 379979
Depth: 12, checked: 921401
Depth: 13, checked: 2209856
Depth: 14, checked: 379964
Depth: 15, checked: 921737
```

## Next week
- Finish Kociemba's algorithm  
- Implement Korf's algorithm (hopefully)  
- Hopefully generate the tables  
