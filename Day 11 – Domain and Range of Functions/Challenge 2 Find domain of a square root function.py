from sympy import sqrt, symbols, S, solveset

x = symbols('x')
f = sqrt(x - 3)
domain = solveset(x - 3 >= 0, x, domain=S.Reals)
print(domain)