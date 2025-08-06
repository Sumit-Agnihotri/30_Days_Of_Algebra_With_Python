from sympy import symbols, Eq, solve

x = symbols('x')
a, b, c = 1, 2, 5  # Try different coefficients

equation = Eq(a*x**2 + b*x + c, 0)
roots = solve(equation, x)

print("Roots:", roots)