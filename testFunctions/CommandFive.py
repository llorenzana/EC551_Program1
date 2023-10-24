from sympy import symbols, parse_expr, to_cnf, simplify_logic, to_dnf

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
                maxterm += f"{variables[i]} | "
            elif bit == '1':
                maxterm += f"~{variables[i]} | "

        # Remove the trailing "|"
        maxterms.append(maxterm[:-2])
    
    return expressions, (" | ".join(expressions)) , maxterms , ( " & ".join(maxterms))

minT = input("Enter the Sum of Product Terms separated by a space: ")
v_in = input("Enter input variables separated by a space (Do NOT use 'E', 'I' as an input): ")

minterms, expand_minT, maxterm , expand_maxT= generate_term(list(map(int, minT.split())), v_in.split())
print("Reduced Literals as SOP: ", to_dnf(expand_minT, simplify=True))
