from sympy import symbols
from sympy.logic.boolalg import truth_table, to_cnf
from sympy.logic.boolalg import And, Or, Not

def quine_mccluskey_tt(table, variables):
    return table.quine_mccluskey(variables)

def count_prime_implicants(expression):
    # Get the variables from the expression
    variables = list(expression.free_symbols)

    # Generate the truth table for the expression
    tt = truth_table(expression, variables)

    # Find the CNF form using the sympy to_cnf function
    cnf_form = to_cnf(expression, True)

    # Find the prime implicants
    prime_implicants = quine_mccluskey_tt(tt, variables)

    return len(prime_implicants)

# Example usage:
A, B, C, D = symbols('A B C D')
expression = And(A, B, Or(C, Not(D)))
num_prime_implicants = count_prime_implicants(expression)

print("Number of Prime Implicants:", num_prime_implicants)
