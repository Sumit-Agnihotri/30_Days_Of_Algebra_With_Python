from sympy import symbols, Poly

x = symbols('x')
dividend = Poly(2*x**2 + 3*x + 5)
divisor = Poly(x + 2)

q, r = dividend.div(divisor)

reconstructed = q * divisor + r

print("Matches original?", reconstructed.as_expr() == dividend.as_expr())