from itertools import product
from sympy.logic.boolalg import Or, And, Not
from sympy import symbols, parse_expr, to_cnf, simplify_logic


def generate_minterms(minterms, variables):
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
    
    return expressions, (" | ".join(expressions))

minT = input("Enter the Sum of Product Terms separated by a space: ")
v_in = input("Enter input variables separated by a space (Do NOT use 'E', 'I' as an input): ")

minterms, expand_minT= generate_minterms(list(map(int, minT.split())), v_in.split())
print("complete: ", simplify_logic(expand_minT))

# Usage:
