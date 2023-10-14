from sympy.logic.boolalg import to_cnf
from sympy.logic.boolalg import simplify_logic
from sympy.abc import symbols

def generate_minterms(minterms, variables):
    minterms = sorted(set(minterms))
    expressions = []

    for minterm in minterms:
        binary_minterm = format(minterm, f'0{len(variables)}b')
        expression = " & ".join([f"~{var}" if bit == '0' else f"{var}" for var, bit in zip(variables, binary_minterm)])
        expressions.append(expression)

    return expressions, " | ".join(expressions)

def reduced_minterms(minterms):
    return simplify_logic(to_cnf(minterms))

# Example usage:
mint = input("Enter the Sum of Product Terms: ")
v_in = input("Enter input variables separated by a space: ")

try:
    minterms = list(map(int, mint.split()))
    variables = v_in.split()

    if not all(isinstance(m, int) for m in minterms):
        raise ValueError("Minterms must be integers.")
    
    expressions, result = generate_minterms(minterms, variables)
    reduced_result = reduced_minterms(result)

    print("Canonical SOP: ", reduced_result)

except ValueError as e:
    print(f"Error: {e}")
