from sympy import symbols, Poly

x = symbols('x')
dividend = Poly(6*x**2 + 5*x + 1)
divisor = Poly(2*x + 1)

quotient, remainder = dividend.div(divisor)

print("Quotient:", quotient.as_expr())
print("Remainder:", remainder.as_expr())