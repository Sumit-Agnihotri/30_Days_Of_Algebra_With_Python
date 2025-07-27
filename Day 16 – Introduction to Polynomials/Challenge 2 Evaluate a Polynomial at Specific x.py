from sympy import symbols, Poly

x = symbols('x')
poly = Poly(3*x**2 + 2*x - 5)

value = poly.eval(2)
print("P(2) =", value)