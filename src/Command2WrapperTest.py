import os
import re
import numpy as np  

from blif_to_tt import blif_file_to_tt_file

# Change the working directory to the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

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

    # PARSE the output file
    # Open a file in read mode ('r')

    # Declare variables needed for parsing
    outputArray = None
    numInputs = None
    numOutputs = None

    with open(outputFilename, 'r') as file:
        
        lineNum = 1 # track line number for parsing
        index = -5 # track the minterm currently being evaluated

        for line in file:
            # Print out the line for debugging 
            print(line, end='')
            
            if lineNum == 2: # Line 2 has number of inputs
                numInputs = int(line[16:-1])
            elif lineNum == 3: # Line 3 has number of outputs
                numOutputs = int(line[17:-1])
                print(numInputs, numOutputs)
                outputArray = np.zeros((numOutputs, pow(2, numInputs)), dtype=bool) # Each row represents an output, columns represent minterms for that input
            elif lineNum >= 6: # Line 3 has number of outputs
                inputIndex = 0
                for i in range(numOutputs):
                    if (int(line[9 + i])):
                        outputArray[inputIndex][index] = True
                        print(inputIndex, index)
                        print(outputArray[inputIndex][index])
                    inputIndex = inputIndex + 1
            else:
                print('We do not care about this line.')
            lineNum = lineNum + 1
            index = index + 1
    
    print(outputArray)
    #Clean up files
    # os.remove(outputFilename)

if __name__ == "__main__":
    main()