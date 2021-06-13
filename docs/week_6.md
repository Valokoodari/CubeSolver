# Weekly report 6  

## What did I do this week?  
| Date  | Time (h) | Task
| :---: | :---     | :---
| 12.6. | 1        | Finally figured out the bug that some orientations are not checked...
| 13.6. | 2.5      | Inefficient table generation for Korf's algorithm and some other small changes.
|       | 0.5      | Continuous progress reporting for Kociemba's algorithm.
| Total | 4        |

## Progress on the program  
- Fixed the most annoying bug... By changing "break" to "continue"... Argh...  
- Some kind of table generation for Korf's algorithm.  

## What did I learn?  
- Always check the code for breaks which shouldn't be there...  

## Challenges?  
- Pylint can't handle large lists  
- The temporary pruning requires over 16 GB of memory at depth 8 (out of 12) in 
  phase 1 and depth 15 (out of 18) in phase 2.  
- Pruning while generating pruning tables is hard  

## Next week  
- Testing on Windows?  
