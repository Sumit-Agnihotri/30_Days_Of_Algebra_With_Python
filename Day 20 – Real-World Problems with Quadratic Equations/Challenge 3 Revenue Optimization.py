from sympy import symbols, Eq, solve

x = symbols('x')
R = (200 - 10*x)*(100 + 5*x)
R_exp = R.expand()
vertex_x = -R_exp.as_poly().coeffs()[1] / (2 * R_exp.as_poly().coeffs()[0])
max_revenue = R.subs(x, vertex_x)

print("Best x (₹10 cuts):", vertex_x)
print("Maximum Revenue: ₹", max_revenue)