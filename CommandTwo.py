def minterms_to_pos_expression(minterms, variables):
    # Sort and remove duplicates from the list of minterms
    num_vars = len(variables)
    all_values = list(range(2 ** num_vars - 1, -1 , -1))
    # Remove values that are in minterms to get maxterms
    remaining_values = [value for value in all_values if value not in minterms]
    expressions = []
    # Convert each maxterm to a boolean expression
    for maxterm in remaining_values:
        # Convert the maxter, to binary and pad with zeros to match the number of variables
        binary_maxterm = format(maxterm, '0b').zfill(num_vars)

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                expression += f"{variables[i]} + "
            elif bit == '1':
                expression += f"~{variables[i]} + "

        # Remove the trailing "|"
        expressions.append(expression[:-2])

    # Combine the boolean expressions using AND operations
    product_of_sums = ") & ( ".join(expressions)

    return product_of_sums

#User In
mint = input("Enter the product of minterms separated by space: ")
v_in = input("Enter input variables separated by a space: ")
pos_expression = minterms_to_pos_expression(list(map(int, mint.split())), v_in.split())
print("Canonical POS expression: (", pos_expression, ")")
