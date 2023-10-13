import sympy

def solve_quadratic(a, b, c):
    # Define variables
    x = sympy.symbols('x')

    # Create the quadratic equation
    equation = a * x**2 + b * x + c

    # Solve the equation
    solutions = sympy.solve(equation, x)

    return solutions

a = 1
b = -3
c = 2

solutions = solve_quadratic(a, b, c)
print("Solutions:", solutions)