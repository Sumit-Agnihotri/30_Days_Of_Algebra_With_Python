from sympy import symbols, And, solve_univariate_inequality

x = symbols('x')
# Solve each part of the compound inequality separately
sol1 = solve_univariate_inequality(3 < 2 * x + 1, x, relational=False)
sol2 = solve_univariate_inequality(2 * x + 1 < 9, x, relational=False)

# Find the intersection of the two solutions
solution = sol1.intersect(sol2)
print("Solution:", solution)