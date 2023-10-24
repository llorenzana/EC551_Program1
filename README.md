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

## Boolean Algebra SOP
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

## BLIF File
### Overview
In this, the program will take in a BLIF file and return one of the 12 commands. It uses code provided [here](https://github.com/IamFlea/BLIF-to-truth-table/blob/master/blif_to_tt.py) to convert the BLIF to a truth table, then parses the truth table in order to obtain the minterms for the function.

The minterms are stored in a matrix where each row represents one output and each column represents a combination of inputs.

The commands are redudant in purpose to those presented in the Boolean Algebra SOP section. The difference is that each function is enclosed in a loop so that each output can be evaluated individually.

## Commands
### Command One
Boolean Algebra:
* Prints the Canonical SOP using Sigma notation
* Prints an expanded Canonical SOP, that results from the BooleanFunction Class
  ```
    boolean_function = BooleanFunction(expression, vars)
    minTerms, CSOP, maxTerms, CPOS = boolean_function.generateTerms()
    print("Canonical SOP: \u03A3 m",  [int(minterm, 2) for minterm in minT])
    print("canonical SOP: ", CSOP)
  ```
BLIF File:
* Prints the Canonical SOP using Sigma notation
* Prints an expanded Canonical SOP, that results from the generate_termBLIF Function
```
    minT = getMintermsFromTT(outputArray[index])
    maxT = getMaxtermsFromTT(outputArray[index])
    _, expand_minT, _, _ = generate_termBLIF(minT, maxT, inputVariableArray)
    print(f"{row} minterms:")
    print("Canonical SOP: \u03A3 m", minT)
    print("canonical SOP: ", expand_minT)
```


## Command Two
Boolean Algebra:
* Prints the Canonical SOP using Capital Pi notation
* Prints an expanded Canonical POS, that results from the BooleanFunction Class
```
    print("Canonical POS: \u03A0 M",  [int(maxterm, 2)for maxterm in maxT])
    print("Canonical POS expression: ", CPOS )
```
BLIF File:
* Prints the Canonical POS using Capital PI notation
* Prints an expanded Canonical POS, that results from the generate_termBLIF Function
```
    minT = getMintermsFromTT(outputArray[index])
    maxT = getMaxtermsFromTT(outputArray[index])
    _, _, _, expand_maxT = generate_termBLIF(minT, maxT, inputVariableArray)
    print(f"{row} maxterms:")
    print("Canonical POS: \u03A0 M",  maxT)
    print("Canonical POS expression: ", expand_maxT)
```

## Command Three
Boolean Algebra:
* Calulates and returns inverse SOP using the **MAXTERMS** produced in the BooleanFunction Class

BLIF File:
* Calulates and returns inverse SOP using the **MAXTERMS** produced in the  generate_termBLIF Function
 
```
calculate_inverse_SOP(maxTerms, vars)
```


## Command Four
Boolean Algebra:
* Calulates and returns inverse POS using the **MINTERMS** produced in the BooleanFunction Class
 
BLIF File:
* Calulates and returns inverse POS using the **MINTERMS** produced in the  enerate_termBLIF Function
*
```
calculate_inverse_POS(minTerms, vars)
```

**
## Command Five
Boolean Algebra:
* Calculates the Reduced SOP Expression using the built in sympy **to_dnf** function
* Returns the number of literals saved in comparison to the canoninical Form
```
minSOP = to_dnf(CSOP, simplify=True, force=True)
print("Reduced Literals as SOP: ", minSOP)
print("Saved Number of literals: ", countLiterals(minT, str(minSOP) , vars))
```
BLIF File:
* Calculates the Reduced SOP Expression using the built in sympy **to_dnf** function
* Returns the number of literals saved in comparison to the canoninical Form
```
 minSOP = to_dnf(expand_minT, simplify=True, force=True)
print(f"{row} Reduced Literals as SOP: ", minSOP)
print(f"{row} Saved Number of literals: ", countLiterals(minT, str(minSOP) , inputVariableArray))
```
## Command Six:
Boolean Algebra:
* Calculates the Reduced POS Expression using the built in sympy **to_cnf** function
* Returns the number of literals saved in comparison to the canoninical Form
```
minPOS = to_cnf(CSOP, simplify= True, force=True)
print("Reduced Literals as POS: ", minPOS)
print("saved number of literals: ", countLiterals(maxT, str(minPOS) , vars))
```

BLIF File:
** Calculates the Reduced POS Expression using the built in sympy **to_cnf** function
* Returns the number of literals saved in comparison to the canoninical Form
```
minPOS = to_cnf(expand_maxT, simplify= True, force=True)
print(f"{row} Reduced Literals as POS: ", minPOS)
print(f"{row} saved number of literals: ", countLiterals(maxT, str(minPOS) , inputVariableArray))
```
## Command Seven:
Boolean Alegbra:
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)

```
PI, _ =  countPI_EPI([int(minterm, 2) for minterm in minT] )
print("Number of Prime Implicants:", len(PI))
```

BLIF File:
* Done for each row of the file
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)
```
PI, _ =  countPI_EPI(minT)
print(f"{row} Number of Prime Implicants:", len(PI))
```

## Command Eight:
Boolean Algebra
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)
```
_, EPI =  countPI_EPI([int(minterm, 2) for minterm in minT] )
        print("Number of Essential Prime Implicants:", len(EPI))
```

BLIF File:
* Done for each row of the file
* Returns the Number of Prime Implicants
* Uses adjusted source code of the quine mcklusky aglorithm (see references)

```
_, EPI =  countPI_EPI(minT)
print(f"{row} Number of Prime Implicants:", len(EPI))
```
## Command Nine:
Boolean Algebra :
* Returns the number of ON-Set **MINTERMS**
```
print("Number of ON-Set minterms: ", len(minT))
```
BLIF File:
* Returns for each row of the file
```
print(f"{row} Number of ON-Set minterms: ", len(minT))
```
## Command Ten:
Boolean Algebra:
* Returns the number of ON-set **MAXTERMS**
```
print("Number of ON-Set maxterms: ", len(maxT))
```

BLIF File:
* Returns for each row of the file
* Returns the number of ON-set **MAXTERMS**
```
print(f"{row} Number of ON-Set maxterms: ", len(maxT))
```
## Command 11:
Boolean Algebra
* Uses the printTT function, which evaluates if each table row is included in the minterms for the function. 
```
printTT([int(minterm, 2) for minterm in minT], len(vars))
```
```
    output = False

    # Generate all possible combinations of inputs
    inputsBinary = list(product([0, 1], repeat=numInputs))

    # Create the header of the truth table
    header = [f'Input_{i}' for i in range(numInputs)] + ['Output']

    # Print the header
    print("\t".join(header))

    # Evaluate minterms and create the truth table
    for index, inputs in enumerate(inputsBinary):
        if index in terms:
            output = True
        row = "\t".join([str(i) for i in inputs] + [str(output)])
        output = False
        print(row)
```
BLIF File:
* Uses the printTTMultiOutput, which bases output on the outputArray from pasing the BLIF file. This array is already in terms of True/False for each minterm, so it simply prints the results for each row.
* The isInverse variable is set to 0, because we are finding the table for the original function.
```
 printTTMultiOutput(outputArray, inputVariableArray, outputVariableArray, 0)
```
```
def printTTMultiOutput(outputArray, inputVariableArray, outputVariableArray, isInverse):
    #Declare vars for correct
    output = False

    # Generate all possible combinations of inputs
    inputsBinary = list(product([0, 1], repeat=len(inputVariableArray)))

    # Create the header of the truth table
    header = [f'{input_variable}' for input_variable in inputVariableArray] + [f'out_{output_variable}' for output_variable in outputVariableArray]

    # Print the header
    print("\t".join(header))

    # Evaluate minterms and create the truth table
    for index, inputsBinary in enumerate(inputsBinary): # Loop for each possible input combination
        row = "\t".join([str(i) for i in inputsBinary])

        for outputIndex, output_variable in enumerate(outputVariableArray):
            if isInverse:
                row += "\t" + str(~outputArray[outputIndex][index])
            else:
                row += "\t" + str(outputArray[outputIndex][index])
                                
        output = False
        print(row)
```
## Command 12:
Boolean Algebra
* Uses the printTT function, which evaluates if each table row is included in the minterms for the function
* We use the current function's maxterms to to evaluate the truth table for the inverse because the maxterms of this function are the minterms of the inverse
```
printTT([int(maxterm, 2) for maxterm in maxT], len(vars))
```

BLIF File:
* This uses the same function as in Command 11, but we are getting the truth table for the inverse, so isInverse is set to true.
```
printTTMultiOutput(outputArray, inputVariableArray, outputVariableArray, 1)
```
## Testcases: 
4-input: 
    
    (A & ~B) | (~C & D) | (~A & B & C) | (~A & B & ~C)
    
    (A & ~B & C) | (~A & B & D) | (~A & ~C & D) | (A & ~B & ~D)
    
    (A & B) | (~B & C & D) | (~A & ~C & D) | (~A & B & ~C) | (~A & ~B & C)

5-input:
    
    (A & B & ~C) | (~B & C & D) | (A & ~C & ~F)
    
    (A & B & ~C) | (~B & C & D) | (~A & ~C & F) | (A & ~B & ~D) | (~A & B & ~F)
    
    
7-input: 

    (A & B & ~C & D) | (~B & C & D & ~F) | (~A & ~C & F & G) | (A & ~B & ~D & ~G) | (~A & B & ~F & H) | (A & ~C & G & H) | (~A & ~B & C & ~H) | (~A & B & ~D & F)

'''


## References  
BLIF Documentation: https://course.ece.cmu.edu/~ee760/760docs/blif.pdf  
BLIF parsing: https://github.com/IamFlea/BLIF-to-truth-table/blob/master/blif_to_tt.py
EPI and PI Finder: https://github.com/int-main/Quine-McCluskey/blob/master/Quine%20McCluskey.py 
