import os
import re
import numpy as np
from itertools import product

from blif_to_tt import blif_file_to_tt_file

# Change the working directory to the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# OUTPUT BELOW THIS LINE
def printTTMultiOutput(terms, numInputs, outputArray):
    #Declare vars for correct scope
    output = False

    # Generate all possible combinations of inputs
    inputsBinary = list(product([0, 1], repeat=numInputs))

    # Create the header of the truth table
    header = [f'Input_{i}' for i in range(numInputs)] + ['Output']

    # Print the header
    print("\t".join(header))

    # Evaluate minterms and create the truth table
    for index, inputs in enumerate(inputsBinary): # Loop for each possible input combination
        if index in terms:
            output = True
        row = "\t".join([str(i) for i in inputs] + [str(output)])
        output = False
        print(row)

# Define the number of variables and minterms
num_variables = 5  # Change this to the number of variables you have
minterms = [0, 1, 2, 3, 5, 10]  # Change this to your list of minterms
printTTMultiOutput(minterms, num_variables)

def printTT(terms, numInputs):
    # Generate all possible combinations of inputs
    inputsBinary = list(product([0, 1], repeat=numInputs))

    # Create the header of the truth table
    header = [f'Input_{i}' for i in range(numInputs)] + ['Output']

    # Print the header
    print("\t".join(header))

    # Evaluate minterms and create the truth table
    for index, inputs in enumerate(inputsBinary): # Loop for each possible input combination
        if index in terms:
            output = True
        row = "\t".join([str(i) for i in inputs] + [str(output)])
        output = False
        print(row)
        
def getMintermsFromTT(boolList): # Produces a list of minterms when given a list
    # Create a list of indices where the value is True
    minterms = [i for i, value in enumerate(boolList) if value]
    return minterms

def getMaxtermsFromTT(boolList): # Produces a list of maxterms when given a list
    # Create a list of indices where the value is False
    maxterms = [i for i, value in enumerate(boolList) if ~value]
    return maxterms

def generate_termBLIF(minterms, maxterms, variables):
    num_vars = len(variables)
    #calculate Minterms
    minterms = sorted(set(minterms))
    binaryMNT = []
    for minterm in minterms:
        binary_minterm = format(minterm, '0b').zfill(len(variables))
        binaryMNT.append(binary_minterm)
    
    binaryMXT = []
    for maxterm in maxterms: 
        binary_minterm = format(maxterm, '0b').zfill(len(variables))
        binaryMXT.append(binary_minterm)  
        
    return binaryMNT, binaryMXT

def main():
    print(f"You chose option 2, command 1. Performing function for Digital Combination Logic Circuit.")

    # Specify the directory path
    folder_path = "blif"

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

   # Print the list of files
    iter = 0
    print(f"Select a file to use:")
    for index, file in enumerate(files):
        print(f"{index + 1}: {file}")

    # Get and error check user choice (DOES NOT CHECK IF FILE IS BLIF)
    while True:
        fileChoice = int(input("Enter your selection: "))

        #Error check user choice
        fileChoice = fileChoice - 1 #Set choice to python indexing

        if (fileChoice >= 0 and fileChoice < len(files)):
            break
        else:
            print("Please select a valid file.")

    # Get the truth table for the selected file
    filename = "blif/" + files[fileChoice]
    outputFilename = files[fileChoice] + ".text"
    blif_file_to_tt_file(filename, outputFilename)

    # Declare variables needed for parsing
    outputArray = None
    numInputs = None
    numOutputs = None
    variableArray = None

    # Parse the file
    with open(outputFilename, 'r') as file:
        lineNum = 1 # track line number for parsing
        index = -5 # track the minterm currently being evaluated, start at -5 because first 5 lines are metadata

        for line in file:
            # Print out the line for debugging 
            if lineNum == 2: # Line 2 has number of inputs
                numInputs = int(line[16:-1])
            elif lineNum == 3: # Line 3 has number of outputs
                numOutputs = int(line[17:-1])
                outputArray = np.zeros((numOutputs, pow(2, numInputs)), dtype=bool) # Each row represents an output, columns represent minterms for that input
                mintermArray = np.full((numOutputs, pow(2, numInputs)), None, dtype=object) # Will fill with minterms for each output
            elif lineNum == 4: # Line 4 has variable names
                pattern = r"Input names: \[([^\]]+)\]"
                match = re.search(pattern, line)

                if match:
                    # Extract and split the names, remove single quotes, and store them in an array
                    variableArray = [name.strip(" '") for name in match.group(1).split(', ')]
                else:
                    print("No input names found in the text.")
                    
            elif lineNum >= 6: # Line 6 + has table outputs
                inputIndex = 0
                for i in range(numOutputs):
                    if (int(line[9 + i])):
                        outputArray[inputIndex][index] = True
                    inputIndex = inputIndex + 1
            lineNum = lineNum + 1
            index = index + 1

    # LOOP TO GET TO ALL INPUTS
    for index, row in enumerate(variableArray):
        # Code that repeats for each varaible below
        print(f"{row} minterms:")
        minT = getMintermsFromTT(outputArray[index])
        print(minT)
        print(f"{row} maxterms:")
        maxT = getMaxtermsFromTT(outputArray[index])
        print(maxT)
        print(index)

    #Clean up files
    os.remove(outputFilename)

if __name__ == "__main__":
    main()