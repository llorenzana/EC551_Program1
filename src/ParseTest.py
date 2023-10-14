from itertools import product
from sympy.logic.boolalg import Or, And, Not
from sympy import symbols, parse_expr, to_cnf, simplify_logic

class BooleanFunction:
    def __init__(self, expression, variables):
        self.expression = expression
        self.variables = variables

    def generate_minterms(self):
        minterms = []

        num_variables = len(self.variables)
        truth_values = list(product([0, 1], repeat=num_variables))

        for values in truth_values:
            assignment = dict(zip(self.variables, values))
            result = eval(self.expression, assignment)

            if result == 1:
                minterm = ''.join(str(value) for value in values)
                minterms.append(minterm)

        # Convert minterms to an expanded sum of minterms
        expanded_sum_of_minterms = self.expand_minterms(minterms)

        return minterms, expanded_sum_of_minterms

    def expand_minterms(self, minterms):
        expanded_sum_of_minterms = []

        for minterm in minterms:
            term = ""
            for i, value in enumerate(minterm):
                if value == '0':
                    term += f"~{self.variables[i]}   "
                elif value == '1':
                    term += f"{self.variables[i]}   "
            # Remove the trailing "&"
            term = term[:-2]
            expanded_sum_of_minterms.append(term)

        return " + ".join(expanded_sum_of_minterms)

# Example usage:
print("Welcome: Please select which you would like to do 1 or 2")
expression = input("Boolean Equation, please use ~ to indicate a NOT: ")
v_in = input("Enter input variables separated by a space: ")
vars = v_in.split()

boolean_function = BooleanFunction(expression, vars)
mintermsRes, cSOP_res = boolean_function.generate_minterms()

print("Generated Minterms:", mintermsRes)
print("Canonical SOP:", cSOP_res)
