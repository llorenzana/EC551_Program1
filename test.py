from sympy import symbols, parse_expr, to_cnf, simplify_logic, to_dnf
from sympy import symbols, parse_expr, to_cnf, simplify_logic, to_dnf

def generate_termBLIF(minterms, maxterms, variables):
    num_vars = len(variables)
    #calculate Minterms
    minterms = sorted(set(minterms))
    binaryMNT = []
    for minterm in minterms:
        binary_minterm = format(minterm, '0b').zfill(len(variables))
        binaryMNT.append(binary_minterm)
    
    binaryMXT = []
    for maxterm in maxterms: 
        binary_minterm = format(maxterm, '0b').zfill(len(variables))
        binaryMXT.append(binary_minterm)  
        
    return binaryMNT, binaryMXT


minterms = [2, 4, 6]
maxterms = [0, 1, 3, 5 , 7]
variables = ['A', 'B', 'C']

binaryMNT, binaryMXT = generate_termBLIF(minterms, maxterms, variables)
print(binaryMNT)
print(binaryMXT)
