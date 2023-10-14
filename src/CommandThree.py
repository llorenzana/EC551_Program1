from itertools import product

def calculate_inverse_SOP(minterms, variables):
    num_vars = len(variables)
    
    all_values = list(range(2 ** num_vars))
    # Remove values that are in minterms to get maxterms
    remaining_values = [value for value in all_values if value not in minterms]
    expressions = []
    # Convert each maxterm to a boolean expression
    for minterm in remaining_values:
        # Convert the maxter, to binary and pad with zeros to match the number of variables
        binary_maxterm = format(minterm, '0b').zfill(num_vars)

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                expression += f"~{variables[i]}  "
            elif bit == '1':
                expression += f"{variables[i]}  "

        # Remove the trailing "+"
        expressions.append(expression[:-2])

    # Combine the boolean expressions using AND operations
    inverse_SOP = ") + ( ".join(expressions)
    return inverse_SOP

minT = input("Enter the minterms separated by space: ")
v_in = input("Enter input variables separated by a space: ")
inverse_SOP = calculate_inverse_SOP(list(map(int, minT.split())), v_in.split())
print("Inverse as a Canonical SOP: (", inverse_SOP, ")")
