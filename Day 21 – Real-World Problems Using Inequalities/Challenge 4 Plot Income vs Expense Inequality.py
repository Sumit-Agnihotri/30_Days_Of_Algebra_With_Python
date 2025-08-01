from sympy import symbols, solve_univariate_inequality, S

misc = symbols('misc')
total = 7000 + 5000 + misc
ineq = total <= 20000
solution = solve_univariate_inequality(ineq, misc, domain=S.Reals)

# Extract the upper bound from the solution
upper_bound = solution.sup if hasattr(solution, 'sup') else solution.args[1]
print("You can spend up to:", upper_bound)