# Example definition for divisor and dividend
from sympy import symbols, Poly

x = symbols('x')
dividend = Poly(2*x**2 + 3*x + 5)
divisor = Poly(x + 2)

q_only = dividend.quo(divisor)
print("Quotient Only:", q_only.as_expr())