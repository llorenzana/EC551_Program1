from sympy import  to_cnf, to_dnf

def generate_termBLIF(minterms, maxterms, variables):
    num_vars = len(variables)
    #calculate Minterms
    minterms = sorted(set(minterms))
    
    binaryMNT = []
    expanded_sum_of_minterms = []
    
    for minterm in minterms:
        binary_minterm = format(minterm, '0b').zfill(len(variables))
        binaryMNT.append(binary_minterm)
        term = ""
        for i, value in enumerate(binary_minterm):
            if value == '0':
                term += f"~{variables[i]} & "
            elif value == '1':
                term += f"{variables[i]} & "
                
        # Remove the trailing "&"
        term = term[:-2]
        expanded_sum_of_minterms.append(term)

    binaryMXT = []
    expanded_POS_Maxterms= []
    # Convert each maxterm to a boolean expression
    for maxT in maxterms:
        binary_maxterm = format(maxT, '0b').zfill(num_vars)
        binaryMXT.append(binary_minterm)
        # Create a boolean expression for the minterm
        maxterm = ""
        for i, bit in enumerate(binary_maxterm):
            if bit == '0':
                maxterm += f"{variables[i]} | "
            elif bit == '1':
                maxterm += f"~{variables[i]} | "

        # Remove the trailing "|"
        expanded_POS_Maxterms.append(maxterm[:-2])

    
    return binaryMNT, (" | ".join(expanded_sum_of_minterms)) , binaryMXT , ( " & ".join(expanded_POS_Maxterms))
    
minterms = [2, 4, 6]
maxterms = [0, 1, 3, 5 , 7]
variables = ['A', 'B', 'C']

binaryMNT, expand_minT, binaryMXT , expand_maxT= generate_termBLIF(minterms, maxterms, variables)

print(binaryMNT)
print(expand_minT)
print(binaryMXT)
print(expand_maxT)

print(to_cnf(expand_minT, simplify=True, force=True)) #use for POS

print(to_dnf(expand_minT, simplify=True, force=True)) #use for SOP

