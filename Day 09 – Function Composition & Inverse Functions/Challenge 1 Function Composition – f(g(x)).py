from sympy import symbols, simplify

x = symbols('x')
f = 2 * x + 3
g = x**2
f_of_g = f.subs(x, g)
g_of_f = g.subs(x, f)
print("f(g(x)) =", simplify(f_of_g))
print("g(f(x)) =", simplify(g_of_f))