from sympy import symbols, Poly

x = symbols('x')
poly = Poly(3*x**2 + 2*x - 5)

print("Polynomial:", poly)
print("Coefficients:", poly.all_coeffs())
print("Degree:", poly.degree())