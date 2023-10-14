from sympy.logic.boolalg import Or, And
from sympy.logic.inference import satisfiable
from sympy.logic.boolalg import to_cnf, simplify_logic
from sympy.abc import symbols
from itertools import product


def generate_minterms(minterms, variables):
    minterms = []

    num_variables = len(variables)
    truth_values = list(product([0, 1], repeat=num_variables))

    for values in truth_values:
        assignment = dict(zip(self.variables, values))
        result = eval(self.expression, assignment)

        if result == 1:
            minterm = ''.join(str(value) for value in values)
            minterms.append(minterm)

    return minterms
    
def minterms_to_expression(minterms, variables):
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

    return " | ".join(expressions)

def reduced_minterms(minterms):
    sop_expression = simplify_logic(to_cnf(minterms))
    return simplify_logic(to_cnf(minterms))

def main():
    mint = input("Enter the Sum of Product Terms: ")
    v_in = input("Enter input variables separated by a space: ")

    try:
        minterms = list(map(int, mint.split()))
        variables = v_in.split()

        if not all(isinstance(m, int) for m in minterms):
            raise ValueError("Minterms must be integers.")
        
        test = minterms_to_expression(minterms, variables)
        result = reduced_minterms(test)

        print("Canonical SOP: ", result)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
