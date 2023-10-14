
def generate_term(minterms, variables):
    num_vars = len(variables)
    #calculate Minterms
    minterms = sorted(set(minterms))
    expressions = []
    
    for minterm in minterms:
        binary_minterm = format(minterm, '0b').zfill(len(variables))
        expression = ""
        for i, bit in enumerate(binary_minterm):
            if bit == '0':
                expression += f"~{variables[i]} & "
            elif bit == '1':
                expression += f"{variables[i]} & "
        expressions.append(expression[:-2])
    
    #maxterms
    all_values = list(range(2 ** num_vars - 1, -1 , -1))
    remaining_values = [value for value in all_values if value not in minterms]
    maxterms = []
    
    # Convert each maxterm to a boolean expression
    for maxT in remaining_values:
        binary_maxterm = format(maxT, '0b').zfill(num_vars)

        # Create a boolean expression for the minterm
        maxterm = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                maxterm += f"{variables[i]} + "
            elif bit == '1':
                maxterm += f"~{variables[i]} + "

        # Remove the trailing "|"
        maxterms.append(maxterm[:-2])
    
    return expressions, ("  |  ".join(expressions)) , maxterms , ( "  &  ".join(maxterms))

mint = input("Enter the Sum of Product Terms: ")
v_in = input("Enter input variables separated by a space: ")
minterms, expandMin, maxterms, expandMax = generate_term(list(map(int, mint.split())), v_in.split())
print("Canonical POS expression: ", expandMax )