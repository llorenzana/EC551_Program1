import os
import numpy as np  
from itertools import product, combinations
from sympy.logic.boolalg import to_cnf, to_dnf,  simplify_logic
from sympy.abc import symbols
from sympy import Or, And
from blif_to_tt import blif_file_to_tt_file

# Change the working directory to the directory where your script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def getMintermsFromTT(boolList): # Produces a list of minterms when given a list
    # Create a list of indices where the value is True
    minterms = [i for i, value in enumerate(boolList) if value]
    print(minterms)
    return minterms

def getMaxtermsFromTT(boolList): # Produces a list of minterms when given a list
    # Create a list of indices where the value is True
    maxterms = [i for i, value in enumerate(boolList) if ~value]
    print(maxterms)
    return maxterms

def perform_main_option_1(choice):
    print(f"You chose option 1, command {choice}. Performing function for Boolean Algebraic Function - MIN SOP.")
    print("Enter the Boolean Equation, Do NOT use 'E', 'I' as an input), ")
    expression = input("each separated by a space and use '~' to indicate a NOT (i.e. A | B & ~C) : ")
    v_in = input("Enter input variables as capital letter separated by a space (Do NOT use 'E', 'I' as an input): ")   
    vars = v_in.split()
    
    #calculates minterms, masxterms, Canonical SOP and Canonical POS
    boolean_function = BooleanFunction(expression, vars)
    minT, CSOP, maxT, CPOS = boolean_function.generateTerms()
        
    if choice == 1: 
        print("Canonical SOP: \u03A3 m",  [int(minterm, 2) for minterm in minT])
        print("canonical SOP: ", CSOP, "")
        
    elif choice == 2: 
        print("Canonical POS: \u03A0 M",  [int(maxterm, 2)for maxterm in maxT])
        print("Canonical POS expression: ", CPOS )
    
    elif choice == 3:
        print("Inverse as a Canonical SOP: (", calculate_inverse_SOP(maxT, vars), ")")

    elif choice == 4: 
        print("Inverse as a Canonical POS: (", calculate_inverse_POS(minT, vars), ")")

    elif choice == 5: 
        minSOP = to_dnf(CSOP, simplify=True, force=True)
        print("Reduced Literals as SOP: ", minSOP)
        print("Saved Number of literals: ", countLiterals(minT, str(minSOP) , vars))
        
    elif choice == 6: 
        minPOS = to_cnf(CSOP, simplify= True, force=True)
        print("Reduced Literals as POS: ", minPOS)
        print("saved number of literals: ", countLiterals(maxT, str(minPOS) , vars))

    elif choice == 7: 
        PI, _ =  countPI_EPI([int(minterm, 2) for minterm in minT] )
        print("Number of Prime Implicants:", len(PI))
        
    elif choice == 8:
        _, EPI =  countPI_EPI([int(minterm, 2) for minterm in minT] )
        print("Number of Essential Prime Implicants:", len(EPI))

    elif choice == 9:
        print("Number of ON-Set minterms: ", len(minT))
    elif choice == 10: 
        print("Number of ON-Set maxterms: ", len(maxT))
    #elif choice == 11:  
    
    else:
        print("Break") 

def perform_main_option_2(choice):
    print(f"You chose option 2, command {choice}. Performing function for Digital Combination Logic Circuit.")

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
            
    # Clean up files
    os.remove(outputFilename)

    #if choice == 1: 

    #elif choice == 2: 
    
    #elif choice == 3:

    #elif choice == 4: 

    #elif choice == 5: 
    
    #elif choice == 6: 
    
    #elif choice == 7: 
    
    #elif choice == 8:
    
    #elif choice == 9:
    
    #elif choice == 10: 
    
    #elif choice == 11:  
    
    #else:
        
##functions: 

##general initizalization - commadn 1 and 2 plus output used in other commands 
class BooleanFunction:
    def __init__(self, expression, variables):
        self.expression = expression
        self.variables = variables

    def generateTerms(self):
        minterms = []
        maxterms = []

        num_variables = len(self.variables)
        truth_values = list(product([0, 1], repeat=num_variables))

        for values in truth_values:
            assignment = dict(zip(self.variables, values))
            result = eval(self.expression, assignment)

            if result == 1:
                minterm = ''.join(str(value) for value in values)
                minterms.append(minterm)
                
            if result == 0:
                maxterm = ''.join(str(value) for value in values)
                maxterms.append(maxterm)
    
        # Convert minterms to an expanded sum of minterms
        expanded_sum_of_minterms = self.expand_minterms(minterms)
        expanded_product_of_maxterms = self.expand_maxterms(maxterms)

        return minterms, expanded_sum_of_minterms , maxterms, expanded_product_of_maxterms

    def expand_minterms(self, minterms):
        expanded_sum_of_minterms = []

        for minterm in minterms:
            term = ""
            for i, value in enumerate(minterm):
                if value == '0':
                    term += f"~{self.variables[i]} & "
                elif value == '1':
                    term += f"{self.variables[i]} & "
                    
            # Remove the trailing "&"
            term = term[:-2]
            expanded_sum_of_minterms.append(term)

        return "  | ".join(expanded_sum_of_minterms)

    def expand_maxterms(self, maxterms):
        expanded_product_of_maxterms = []

        for maxterm in maxterms:
            term = ""
            for i, value in enumerate(maxterm):
                if value == '0':
                    term += f"{self.variables[i]} | "
                elif value == '1':
                    term += f"~{self.variables[i]} | "

            # Remove the trailing "|"
            term = term[:-2]
            expanded_product_of_maxterms.append(term)

        return "  &  ".join(expanded_product_of_maxterms)   

##inverse calcs cooand 3-4
def calculate_inverse_SOP(maxterms, variables):
        inverse_SOP = []
        
        for maxterm in maxterms:
            term = ""
            for i, value in enumerate(maxterm):
                if value == '0':
                    term += f"~{variables[i]} & "
                elif value == '1':
                    term += f"{variables[i]} & "
           
            term = term[:-2]
            inverse_SOP.append(term)
        
        return " ) | (".join(inverse_SOP)

def calculate_inverse_POS(minterms, variables): 
    inverse_POS = []
    # Convert each maxterm to a boolean expression
    for minterm in minterms:
        # Convert the maxter, to binary and pad with zeros to match the number of variables
        term = ""
        for i, value in enumerate(minterm):
            if value == '0': 
                term += f"{variables[i]}  | "
            elif value == '1': 
                term += f"~{variables[i]}  | " 
        
        term = term[:-2]
        inverse_POS.append(term)
    return ") & ( ".join(inverse_POS)

# use for commands 5 and 6
def countLiterals(minterms, simplified, variables):
    canonicalCount = len(variables) * len(minterms)
    minimizedCount = sum(simplified.count(var) for var in variables)
    return (canonicalCount - minimizedCount)

# number of prime implicants & essential prime implicants
def countPI_EPI(mt):
    def findEPI(x): #EPI function
        EPI = []
        for i in x:
            if len(x[i]) == 1: ##checks if its is only one --> means its EPI
                if x[i] not in EPI: ## doesn't append if already there 
                    EPI.append(x[i]) ## apend value
        return EPI

    def flatten(x): # Flattens list
        return [item for sublist in x.values() for item in sublist]

    def findminterms(a): #Function for finding out which minterms are merged
        gaps = a.count('-')
        if gaps == 0:
            return [str(int(a,2))]
        x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
        temp = []
        for i in range(pow(2,gaps)):
            temp2,ind = a[:],-1
            for j in x[0]:
                if ind != -1:
                    ind = ind+temp2[ind+1:].find('-')+1
                else:
                    ind = temp2[ind+1:].find('-')
                temp2 = temp2[:ind]+j+temp2[ind+1:]
            temp.append(str(int(temp2,2)))
            x.pop(0)
        return temp

    def compare(a,b): # Function for checking if 2 minterms differ by 1 bit only
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                mismatch_index = i
                c += 1
                if c>1:
                    return (False,None)
        return (True,mismatch_index)
         
    mt.sort()
    minterms = mt
    minterms.sort()
    size = len(bin(minterms[-1]))-2
    groups, all_pi = {},set()

    # Primary grouping starts
    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]

    while True:
        tmp = groups.copy()
        groups,m,marked,should_stop = {},0,set(),True
        l = sorted(list(tmp.keys()))
        for i in range(len(l)-1):
            for j in tmp[l[i]]: # Loop which iterates through current group elements
                for k in tmp[l[i+1]]: # Loop which iterates through next group elements
                    res = compare(j,k) # Compare the minterms
                    if res[0]: # If the minterms differ by 1 bit only
                        try:
                            groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None # Put a '-' in the changing bit and add it to corresponding group
                        except KeyError:
                            groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] # If the group doesn't exist, create the group at first and then put a '-' in the changing bit and add it to the newly created group
                        should_stop = False
                        marked.add(j) # Mark element j
                        marked.add(k) # Mark element k
            m += 1
        local_unmarked = set(flatten(tmp)).difference(marked) # Unmarked elements of each table
        all_pi = all_pi.union(local_unmarked) # Adding Prime Implicants to global list
        if should_stop: # If the minterms cannot be combined further
            break        

    # Prime Implicant Chart begin
    sz = len(str(mt[-1])) # The number of digits of the largest minterm --> integer 
    chart = {} # create a chart --> keep track of pi and EPI
    
    for i in all_pi:
        merged_minterms = findminterms(i)
        for j in merged_minterms:
            x = mt.index(int(j))*(sz+1) # The position where we should put 'X'
            try:
                chart[j].append(i) if i not in chart[j] else None # Add minterm in chart
            except KeyError:
                chart[j] = [i]
    # Printing and processing of Prime Implicant chart ends

    EPI = findEPI(chart) # Finding essential prime implicants
    return all_pi, EPI

#Command Line Experience
def main():
    while True:
        print("Input Options:")
        print("1. Boolean Algebraic Function - MIN SOP")
        print("2. Digital Combination Logic Circuit" )
        print("0. Exit \n")

        main_choice = int(input("Enter your input choice: "))

        if main_choice == 0:
            print("Thanks for using our program. Goodbye!")
            break
        
        
        if main_choice == 1 or main_choice == 2:
            print("Commands:")
            print("1. Canonical SOP")
            print("2. Canonocal POS")
            print("3. Inverse as Canonical SOP")
            print("4. Inverse as Canonical POS")
            print("5. Minimized Number of Literals in SOP")
            print("6. Minimized number of literals in POS ")
            print("7. # of Prime Implicants")
            print("8. # of Essential Prime Implcants ")
            print("9. # of ON-Set Minterms")
            print("10. # Of ON-Set Maxterms ")
            print("11. ")
            print("12. \n")

            command = int(input("Enter your command: "))

            if main_choice == 1:
                perform_main_option_1(command)
            elif main_choice == 2:
                perform_main_option_2(command)
            else:
                print("Invalid command. Please enter a valid command.")

        else:
            print("Invalid choice. Please enter a valid main option.")

        another_command = input("Do you want to perform another command? (yes/no): ")
        if another_command.lower() != 'yes':
            print("Thanks for using our program. Goodbye!")
            break

if __name__ == "__main__":
    main()

