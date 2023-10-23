import os
import re
import numpy as np  

from blif_to_tt import blif_file_to_tt_file

# Change the working directory to the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def getMinterms(boolList): # Produces a list of minterms when given a list
    # Create a list of indices where the value is True
    minterms = [i for i, value in enumerate(boolList) if value]
    print(minterms)
    return minterms

def main():
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
        choice = int(input("Enter your selection: "))

        #Error check user choice
        choice = choice - 1 #Set choice to python indexing

        if (choice >= 0 and choice < len(files)):
            break
        else:
            print("Please select a valid file.")

    # Get the truth table for the selected file
    filename = "blif/" + files[choice]
    outputFilename = files[choice] + ".text"
    blif_file_to_tt_file(filename, outputFilename)

    # Declare variables needed for parsing
    outputArray = None
    numInputs = None
    numOutputs = None

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
            elif lineNum >= 6: # Line 3 has number of outputs
                inputIndex = 0
                for i in range(numOutputs):
                    if (int(line[9 + i])):
                        outputArray[inputIndex][index] = True
                    inputIndex = inputIndex + 1
            lineNum = lineNum + 1
            index = index + 1
    
    # Use the arrays to get the minterms //TEST
    print(outputArray[7])
    getMinterms(outputArray[7])

    #Clean up files
    # os.remove(outputFilename)

if __name__ == "__main__":
    main()