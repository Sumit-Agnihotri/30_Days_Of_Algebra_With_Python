from sympy import symbols

x = symbols('x')
fx = 2 * x + 3

print("x\tf(x)")
for val in range(-5, 6):
    print(f"{val}\t{fx.subs(x, val)}")