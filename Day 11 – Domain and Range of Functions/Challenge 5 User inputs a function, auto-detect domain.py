from sympy import sympify, symbols, S
from sympy.calculus.util import continuous_domain

x = symbols('x')
user_input = input("Enter your function in terms of x (e.g., 1/(x-3), sqrt(x+2), Abs(x)):\n")
f = sympify(user_input)

domain = continuous_domain(f, x, S.Reals)
print(f"Domain of f(x) = {f} is:", domain)