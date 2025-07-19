from sympy import symbols, lambdify

x = symbols('x')
f = 2 * x + 3

f_lambdified = lambdify(x, f)
print(f_lambdified(4))  # Evaluating the function at x = 4