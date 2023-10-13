from sympy.logic.boolalg import Or, And, Not
from sympy import to_cnf, simplify_logic, parse_expr

def parse_boolean_expression(expression):
    return parse_expr(expression)

def get_literals(expr):
    return sorted(expr.atoms(), key=lambda x: x.sort_key())

def get_sop(expr):
    sop_terms = []

    def traverse(expr):
        if isinstance(expr, Or):
            for arg in expr.args:
                traverse(arg)
        elif isinstance(expr, And):
            sop_terms.append(expr)

    traverse(expr)
    return sop_terms

def canonical_sop(expr):
    literals = get_literals(expr)
    sop_terms = get_sop(expr)

    canonical_sop_terms = []

    for sop_term in sop_terms:
        product_terms = []

        for literal in literals:
            if literal in sop_term.args:
                product_terms.append(literal)
            elif ~literal in sop_term.args:
                product_terms.append(~literal)

        canonical_sop_terms.append(And(*product_terms))

    return canonical_sop_terms


boolean_expression = "(A & B) | (C & ~D)"
parsed_expression = parse_boolean_expression(boolean_expression)
print("Parsed Expression:", parsed_expression)

cnf_expr = to_cnf(parsed_expression)
print("CNF Form:", cnf_expr)

simplified_expr = simplify_logic(cnf_expr)
print("Simplified Form:", simplified_expr)

print("Literals: ", get_literals(simplified_expr))
print("Some of Products: ", get_sop(simplified_expr))
print ("canonical SOP: ", canonical_sop(simplified_expr))
