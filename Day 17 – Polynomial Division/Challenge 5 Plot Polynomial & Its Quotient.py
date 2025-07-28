import numpy as np
import matplotlib.pyplot as plt
from sympy import Poly, symbols, lambdify

x = symbols('x')

dividend = Poly(2*x**2 + 3*x + 5)
divisor = Poly(x + 2)
q, r = dividend.div(divisor)

# Lambdify
f_dividend = lambdify(x, dividend.as_expr(), 'numpy')
f_quotient = lambdify(x, q.as_expr(), 'numpy')

x_vals = np.linspace(-10, 10, 400)
plt.plot(x_vals, f_dividend(x_vals), label='Dividend')
plt.plot(x_vals, f_quotient(x_vals), '--', label='Quotient')
plt.title("Polynomial vs Quotient")
plt.legend()
plt.grid()
plt.show()