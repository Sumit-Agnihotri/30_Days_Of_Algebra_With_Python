from sympy import symbols, factor

x = symbols('x')
expr = x**2 - 9
factored = factor(expr)
print("Factored form:", factored)