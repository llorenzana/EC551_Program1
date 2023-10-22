from itertools import product
from sympy.logic.boolalg import Or, And, Not
from sympy import symbols, parse_expr, to_cnf, simplify_logic

class BooleanFunction:
    def __init__(self, expression, variables):
        self.expression = expression
        self.variables = variables

    def generateTerms(self):
        minterms = []
        maxterms = []

        num_variables = len(self.variables)
        truth_values = list(product([0, 1], repeat=num_variables))

        for values in truth_values:
            assignment = dict(zip(self.variables, values))
            result = eval(self.expression, assignment)

            if result == 1:
                minterm = ''.join(str(value) for value in values)
                minterms.append(minterm)
                
            if result == 0:
                maxterm = ''.join(str(value) for value in values)
                maxterms.append(maxterm)
    
        # Convert minterms to an expanded sum of minterms
        expanded_sum_of_minterms = self.expand_minterms(minterms)
        expanded_product_of_maxterms = self.expand_maxterms(maxterms)

        return minterms, expanded_sum_of_minterms , maxterms, expanded_product_of_maxterms

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

    def expand_maxterms(self, maxterms):
        expanded_product_of_maxterms = []

        for maxterm in maxterms:
            term = ""
            for i, value in enumerate(maxterm):
                if value == '0':
                    term += f"{self.variables[i]} | "
                elif value == '1':
                    term += f"~{self.variables[i]} | "

            # Remove the trailing "|"
            term = term[:-2]
            expanded_product_of_maxterms.append(term)

        return " & ".join(expanded_product_of_maxterms)
    
    def find_prime_implicants(self):
        simplified_function = simplify_logic(self.expression)

        prime_implicants = simplified_function.args if isinstance(simplified_function, Or) else [simplified_function]

        return len(prime_implicants)

    def find_essential_prime_implicants(self, minterms):
        prime_implicants = self.find_prime_implicants()
        essential_prime_implicants = []

        for minterm in minterms:
            count = 0
            essential_implicant = None
            for prime_implicant in prime_implicants:
                if minterm in prime_implicant.args:
                    count += 1
                    essential_implicant = prime_implicant

            if count == 1:
                essential_prime_implicants.append(essential_implicant)

        return essential_prime_implicants   
         
#  Example usage:
print("Welcome: Please select which you would like to do 1 or 2")
expression = input("Boolean Equation, please use ~ to indicate a NOT: ")
v_in = input("Enter input variables separated by a space: ")
vars = v_in.split()

boolean_function = BooleanFunction(expression, vars)
minterms, CSOP, maxterms, CPOS = boolean_function.generateTerms()

print("Generated Minterms:", minterms)
print("Generated Maxterms:", maxterms)

prime_implicants = boolean_function.find_prime_implicants()
essential_prime_implicants = boolean_function.find_essential_prime_implicants(minterms)

print("Prime Implicants:", prime_implicants)
print("Essential Prime Implicants:", essential_prime_implicants)





