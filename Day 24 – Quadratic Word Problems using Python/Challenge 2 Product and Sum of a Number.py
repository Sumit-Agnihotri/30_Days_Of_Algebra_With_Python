from sympy import symbols, Eq, solve

x = symbols('x')
eq = Eq(x * (x + 1), 132)
solution = solve(eq, x)

print("The numbers are:")
for sol in solution:
    print(f"{int(sol)} and {int(sol) + 1}")