from sympy import symbols, factor

x = symbols('x')
expr = 2*x**2 + 4*x
factored = factor(expr)
print("Factored form:", factored)