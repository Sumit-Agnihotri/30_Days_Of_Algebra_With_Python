from sympy import symbols, factor

x = symbols('x')
expr = x**2 + 5*x + 6

factored = factor(expr)
print("Factored form:", factored)