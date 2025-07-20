from sympy import symbols, Eq, solve

x, y = symbols('x y')
f = Eq(y, 2*x + 3)

inverse_eq = f.subs({y: x, x: y})
inverse_func = solve(inverse_eq, x)[0]

print("Inverse function f⁻¹(x):", inverse_func)