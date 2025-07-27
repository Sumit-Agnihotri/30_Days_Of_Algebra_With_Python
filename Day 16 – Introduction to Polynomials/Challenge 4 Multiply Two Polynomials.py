from sympy import symbols, Poly

x = symbols('x')
p1 = Poly(3*x**2 + 2*x - 5)
p2 = Poly(x**2 - x + 1)


product_poly = p1 * p2
print("Product:", product_poly.as_expr())