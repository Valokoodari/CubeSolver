# Weekly report 6  

## What did I do this week?  
| Date  | Time (h) | Task
| :---: | :---     | :---
| 12.6. | 1        | Finally figured out the bug that some orientations are not checked...
| 13.6. | 2.5      | Inefficient table generation for Korf's algorithm and some other small changes.
|       | 0.5      | Continuous progress reporting for Kociemba's algorithm.
| 14.6. | 1.5      | Docstrings for Korf's algorithm.
|       | 0.5      | Docstrings for Kociemba's algorithm.
|       | 0.5      | Docstrings for everything except the data structures.
|       | 1        | Docstrings for the Cube and CubeFace data structures.
| 18.6. | 1        | Implemented the search with pruning for Korf's algorithm.
|       | 2        | Peer review.
| Total | 10.5     |

## Progress on the program  
- Fixed the most annoying bug... By changing "break" to "continue"... Argh...  
- Some kind of table generation for Korf's algorithm.  
- Korf's algorithm ready apart from the pruning tables.

## What did I learn?  
- Always check the code for breaks which shouldn't be there...  
- I still have no idea how to generate the pruning tables efficiently. :(  

## Challenges?  
- Pylint can't handle large lists (can't lint korf_tables.py)  
- The temporary pruning requires over 16 GB of memory at depth 8 (out of 12) in 
  phase 1 and depth 15 (out of 18) in phase 2.  
- Pruning while generating pruning tables is hard  
- Can't figure out how to calculate the sym-coordinates for Kociemba's 
  algorithm.  

## Next week  
- Try to finish the program. :/
- Testing on Windows?  

## Questions
- Can I still pass the course even if I can't finish my program like it seems at the moment?
