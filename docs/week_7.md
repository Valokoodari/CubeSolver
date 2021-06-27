# Weekly report 7  

## What did I do this week?  
| Date  | Time (h) | Task
| :---: | :---     | :---
| 21.6. | 1.5      | Getting ready for tomorrow's demo
|       | 1        | Update documentation
| 22.6. | 2        | More preparations for the demo.
|       | 2        | The demo session
|       | 3        | 32-bit integer based CubeFace
| 25.6. | 2        | Update documentation
|       | 1.5      | Solve top cross with the simple algorithm
| 26.6. | 1.5      | Solve top corners with the simple algorithm
|       | 3        | Completely solve the cube with the simple algorithm
| 27.6. | 3        | Manual testing and fixing bugs.
|       | 3        | Hunting for bugs and the last tweaks.
| Total | 23.5     |

## Progress on the program  
- A way to run the program without generating the pruning tables.  
- About 30 % performance improvement with the rewritten CubeFace class.  
- The simple algorithm is now able to solve the cube.  
- There are at least partial tables for Korf's algorithm and at least depth 9
  could be generated in somewhat reasonable time on a modern computer.

## What did I learn?  
- Even bitwise operations won't help too much with performance.  

## Challenges?  
- The performance is still quite poor.  

## Summary
Even though I couldn't achieve what I originally aimed for, I still learned a 
lot during this project. And while I hope that I can at least barely pass the 
course with the current state of this project, I'm not going to abandon this. 
I will probably just take a break (don't know when I'll continue but I will) 
from this and make this somehow work in the future. Probably the best way 
forward is to change from Python to Rust or C++ as those are considerably 
faster.  

I must do some more research on how to calculate the cube symmetries and how to 
generate the pruning tables for Kociemba's algorithm as the symmetries and 
the phase 1 minimum distances are a bit harder than I expected. And for Korf's 
algorithm I just have to find a way to generate the complete pruning tables in 
a reasonable time.  

Should have researched this topic more before I chose this. As with enough 
research I would have probably realized how hard this is. (I should have gone 
with the Twitter shitpost AI which was one of my first ideas...)  
