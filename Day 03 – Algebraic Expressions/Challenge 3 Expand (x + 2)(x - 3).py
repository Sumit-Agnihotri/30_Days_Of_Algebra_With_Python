from sympy import symbols

x, y = symbols('x y')
expression = (x + 2) * (x - 3)
expanded_expression = expression.expand()
print(expanded_expression)