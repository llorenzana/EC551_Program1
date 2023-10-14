from sympy import symbols, Or, And, simplify_logic, to_cnf, Not

# Define input variables
n = 5  # the number of variables that are needed
dynamic_vars = symbols(f'A:{n}')

# Define the SOP function
sop_function = Or(And(A, B), And(B, C))
boolean_function = And(A, Or(B, Not(C)))

# Convert to minimal SOP form
msop_function = simplify_logic(sop_function, form='dnf')
pos_form = to_cnf(boolean_function, True)

# Print the minimal SOP function
print(msop_function)
print(pos_form)

