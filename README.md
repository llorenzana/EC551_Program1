# EC551 Program 1
#### Leanorine Lorenzana-Garcia & Cole Wentzel

## Table of Contents  
[Overview](#Overview)  
[Organization](#Organization)  
[Functions](#Functions)  
[References](#References)  


### Testcases: 
2-input:

4-input: 
    (A & ~B) | (~C & D) | (~A & B & C) | (~A & B & ~C)
    (A & ~B & C) | (~A & B & D) | (~A & ~C & D) | (A & ~B & ~D)
    (A & B) | (~B & C & D) | (~A & ~C & D) | (~A & B & ~C) | (~A & ~B & C)


5-input:
    (A & B & ~C) | (~B & C & D) | (A & ~C & ~F)
    (A & B & ~C) | (~B & C & D) | (~A & ~C & F) | (A & ~B & ~D) | (~A & B & ~F)
    
7-input: 
    (A & B & ~C & D) | (~B & C & D & ~F) | (~A & ~C & F & G) | (A & ~B & ~D & ~G) | (~A & B & ~F & H) | (A & ~C & G & H) | (~A & ~B & C & ~H) | (~A & B & ~D & F)
### Overview


### Organization


### Functions  

### References  
BLIF Documentation: https://course.ece.cmu.edu/~ee760/760docs/blif.pdf  
BLIF parsing: https://github.com/IamFlea/BLIF-to-truth-table/blob/master/blif_to_tt.py