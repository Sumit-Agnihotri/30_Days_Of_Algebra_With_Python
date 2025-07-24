# challenge2_sympy_piecewise.py
from sympy import symbols, Piecewise

x = symbols('x')
f = Piecewise((x**2, x < 0), (x + 2, x >= 0))

print("f(x):", f)
print("f(-3):", f.subs(x, -3))
print("f(2):", f.subs(x, 2))