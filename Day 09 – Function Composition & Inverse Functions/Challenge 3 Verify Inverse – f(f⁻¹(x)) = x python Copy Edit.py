from sympy import simplify, symbols

x = symbols('x')
f_inv = (x - 3)/2
f = 2 * x + 3

step1 = f.subs(x, f_inv)
print("f(f⁻¹(x)) =", simplify(step1))  # Should print x