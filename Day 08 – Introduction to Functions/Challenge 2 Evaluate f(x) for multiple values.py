from sympy import symbols, lambdify

x = symbols('x')
f = x**2 - 4*x + 5

f_lambdified = lambdify(x, f)
for val in range(-3, 4):
    print(f"f({val}) = {f_lambdified(val)}")