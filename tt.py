from itertools import product

# OUTPUT BELOW THIS LINE
def printTTMultiOutput(terms, numInputs, outputArray):
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