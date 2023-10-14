from sympy.logic.boolalg import Or, And
from sympy.logic.inference import satisfiable
from sympy.logic.boolalg import to_cnf
from sympy.logic.boolalg import simplify_logic
from sympy.abc import symbols

def minterms_to_expression(minterms, variables):
    # Sort and remove duplicates from the list of minterms
    minterms = sorted(set(minterms))

    # Initialize an empty list to store boolean expressions for each minterm
    expressions = []

    # Convert each minterm to a boolean expression
    for minterm in minterms:
        # Convert the minterm to binary and pad with zeros to match the number of variables
        binary_minterm = format(minterm, '0b').zfill(len(variables))

        # Create a boolean expression for the minterm
        expression = ""
        for i, bit in enumerate(binary_minterm):
            if bit == '0':
                expression += f"~{variables[i]} & "
            elif bit == '1':
                expression += f"{variables[i]} & "

        # Remove the trailing "&" and add the expression to the list
        expressions.append(expression[:-2])

    # Combine the boolean expressions using OR operations
    sum_of_minterms = " | ".join(expressions)

    return sum_of_minterms


def reduced_minterms(minterms):

    # Convert the expression to CNF (Conjunctive Normal Form)
    cnf_expression = to_cnf(minterms)

    sop_expression = simplify_logic(minterms)

    return sop_expression


mint = input("Enter the Sum of Product Terms: ")
v_in = input("Enter input variables separated by a space: ")
test = minterms_to_expression(list(map(int, mint.split())), v_in.split())
result = reduced_minterms(test)
print("Canonical SOP: ", reduced_minterms(minterms_to_expression(list(map(int, mint.split())), v_in.split())))