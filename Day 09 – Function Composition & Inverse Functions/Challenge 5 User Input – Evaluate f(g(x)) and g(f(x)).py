from sympy import symbols, lambdify

x = symbols('x')
f = 2*x + 3
g = x**2

f_l = lambdify(x, f)
g_l = lambdify(x, g)

user_input = int(input("Enter a value for x: "))
print("f(g(x)) =", f_l(g_l(user_input)))
print("g(f(x)) =", g_l(f_l(user_input)))