from sympy import symbols, factor

x = symbols('x')
expr = x**3 - 8
factored = factor(expr)
print("Factored form:", factored)