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

def reduced_minterms(minterms):
    return simplify_logic(to_cnf(minterms))


print("Welcome: Please select which you would like to do 1 or 2")
minT = input("Boolean Equation, please use ~ to indicate a NOT: ")
v_in = input("Enter input variables separated by a space: ")

test, test2= generate_minterms(list(map(int, minT.split())), v_in.split())
print ("Check: ", test2)
print("Generated Minterms:", test)
print("complete: ", reduced_minterms(test2))
