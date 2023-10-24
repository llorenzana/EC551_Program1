from itertools import product

def calculate_inverse_POS(minterms, variables):
    
    # Remove values that are in minterms to get maxterms
    remaining_values = minterms[::-1]
    print(remaining_values)
    expressions = []
    # Convert each maxterm to a boolean expression
    for maxterm in remaining_values:
        # Convert the maxter, to binary and pad with zeros to match the number of variables
        binary_maxterm = format(maxterm, '0b').zfill(len(variables))

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                expression += f"{variables[i]} + "
            elif bit == '1':
                expression += f"~{variables[i]} + "

        # Remove the trailing "+"
        expressions.append(expression[:-2])

    # Combine the boolean expressions using AND operations
    inverse_POS = ") & ( ".join(expressions)
    return inverse_POS

minT = input("Enter the minterms separated by space: ")
v_in = input("Enter input variables separated by a space: ")
inverse_POS = calculate_inverse_POS(list(map(int, minT.split())), v_in.split())
print("Inverse as a Canonical POS: (", inverse_POS, ")")
