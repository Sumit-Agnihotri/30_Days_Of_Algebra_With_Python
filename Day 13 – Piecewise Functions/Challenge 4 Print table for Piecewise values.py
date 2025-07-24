# challenge4_table_piecewise.py
from sympy import symbols, Piecewise

x = symbols('x')
f = Piecewise((x**2, x < 0), (x + 2, x >= 0))

print("x\tf(x)")
for val in range(-5, 6):
    print(f"{val}\t{f.subs(x, val)}")