# EC551 Program 1
#### Leanorine Lorenzana-Garcia & Cole Wentzel

## Table of Contents 
Boolean Algebra SOP
    Overview
    Commands
    Test Cases
    
    
[Overview](#Overview)  
[Organization](#Organization)  
[Functions](#Functions)  
[References](#References)  

# Organziation  
The majority of our code is within the 'src' folder.
``main.py`` stores the main function for the program. Additionally, this folder contains ``blif_to_tt.py``, which is code used to aid in the graph BLIF input. Finally, the folder contains the subfolder 'src/blif', which contains the test BLIF files.

We have included the files we used to test out our functions in the 'testFunctions' folder. 

# Functions  
The functions for this program are broken down below based on the input method chosen.

## Boolean Algebra SOP: 
### Overview 
In this, the program will take in a SOP Function and return one of the 12 commands. It initializes with a BooleanFunction class in which it takes the command line input, parses the SOP equation and produces:
* A list of binary **MINTERMS**
* An expanded Canonical SOP
* A list of binary **MAXTERMS**
* An expanded Canonical POS

```
boolean_function = BooleanFunction(expression, vars)
minTerms, CSOP, maxTerms, CPOS = boolean_function.generateTerms()
```
Using these outputs, we pass them into various command functions to produce the associated results.      

### Commands: 
**Command One:**
* Prints the Canonical SOP using Sigma notation
* Prints an expanded Canonical SOP, that results from the BooleanFunction Class   

**Command Two:**
* Prints the Canonical SOP using Capital Pi notation
* Prints an expanded Canonical POS, that results from the BooleanFunction Class

**Command Three:**
* Calulates and returns inverse SOP using the **MAXTERMS** produced in the BooleanFunction Class
```
calculate_inverse_SOP(maxTerms, vars)
```

**Command Four:**
* Calulates and returns inverse POS using the **MINTERMS** produced in the BooleanFunction Class
```
calculate_inverse_POS(minTerms, vars)
```

**Command Five:**
* Calculates the Reduced SOP Expression using the built in sympy **to_dnf** function
* Returns the number of literals saved in comparison to the canoninical Form
```
minSOP = to_dnf(CSOP, simplify=True, force=True)
print("Reduced Literals as SOP: ", minSOP)
print("Saved Number of literals: ", countLiterals(minT, str(minSOP) , vars))
```

**Command Six:**
* Calculates the Reduced POS Expression using the built in sympy **to_cnf** function
* Returns the number of literals saved in comparison to the canoninical Form
```
minPOS = to_cnf(CSOP, simplify= True, force=True)
print("Reduced Literals as POS: ", minPOS)
print("saved number of literals: ", countLiterals(maxT, str(minPOS) , vars))
```
**Command Seven:**
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)

```
PI, _ =  countPI_EPI([int(minterm, 2) for minterm in minT] )
print("Number of Prime Implicants:", len(PI))
```
**Command Eight:**
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)
```
_, EPI =  countPI_EPI([int(minterm, 2) for minterm in minT] )
        print("Number of Essential Prime Implicants:", len(EPI))
```
**Command Nine:**
*Returns the number of ON-Set **MINTERMS** 
```
print("Number of ON-Set minterms: ", len(minT))
```

**Command 10:**
* Returns the number of ON-set **MAXTERMS**
```
print("Number of ON-Set minterms: ", len(maxT))
```
**Command 11:** 
* 

**Command 12:**
* 

### Testcases: 
4-input: 
    
    (A & ~B) | (~C & D) | (~A & B & C) | (~A & B & ~C)
    
    (A & ~B & C) | (~A & B & D) | (~A & ~C & D) | (A & ~B & ~D)
    
    (A & B) | (~B & C & D) | (~A & ~C & D) | (~A & B & ~C) | (~A & ~B & C)

5-input:
    
    (A & B & ~C) | (~B & C & D) | (A & ~C & ~F)
    
    (A & B & ~C) | (~B & C & D) | (~A & ~C & F) | (A & ~B & ~D) | (~A & B & ~F)
    
    
7-input: 

    (A & B & ~C & D) | (~B & C & D & ~F) | (~A & ~C & F & G) | (A & ~B & ~D & ~G) | (~A & B & ~F & H) | (A & ~C & G & H) | (~A & ~B & C & ~H) | (~A & B & ~D & F)

###
## A Digital Logic Circuit: 
### Overview


### Commands: 
**Command One:**
* Prints the Canonical SOP using Sigma notation
* Prints an expanded Canonical SOP, that results from the BooleanFunction Class   

**Command Two:**
* Prints the Canonical SOP using Capital Pi notation
* Prints an expanded Canonical POS, that results from the BooleanFunction Class

**Command Three:**
* Calulates and returns inverse SOP using the **MAXTERMS** produced in the BooleanFunction Class


**Command Four:**
* Calulates and returns inverse POS using the **MINTERMS** produced in the BooleanFunction Class


**Command Five:**
* Calculates the Reduced SOP Expression using the built in sympy **to_dnf** function
* Returns the number of literals saved in comparison to the canoninical Form


**Command Six:**
* Calculates the Reduced POS Expression using the built in sympy **to_cnf** function
* Returns the number of literals saved in comparison to the canoninical Form

**Command Seven:**
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)


**Command Eight:**
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)

**Command Nine:**
*Returns the number of ON-Set **MINTERMS** 

**Command 10:**
* Returns the number of ON-set **MAXTERMS**

**Command 11:** 
* 

**Command 12:**
* 



### 
### References  
BLIF Documentation: https://course.ece.cmu.edu/~ee760/760docs/blif.pdf  
BLIF parsing: https://github.com/IamFlea/BLIF-to-truth-table/blob/master/blif_to_tt.py
EPI and PI Finder: https://github.com/int-main/Quine-McCluskey/blob/master/Quine%20McCluskey.py 
