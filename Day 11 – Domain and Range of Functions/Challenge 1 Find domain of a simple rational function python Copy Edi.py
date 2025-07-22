from sympy import symbols, S
from sympy.calculus.util import continuous_domain
from sympy import sin

x = symbols('x')
f = 1 / (x - 2)

domain = continuous_domain(f, x, S.Reals)
print("Domain of f(x) = 1 / (x - 2) is:", domain)