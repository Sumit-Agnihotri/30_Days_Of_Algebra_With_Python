from sympy import symbols, simplify, solve

x = symbols('x')
price = 100 - 10*x
people = 200 + 20*x

revenue = simplify(price * people)
print("Revenue equation:", revenue)

# Derivative to find max revenue
revenue_derivative = revenue.diff(x)
optimal_x = solve(revenue_derivative)[0]
max_revenue = revenue.subs(x, optimal_x)

print(f"Best ₹10 cuts: {optimal_x}")
print(f"Max Revenue: ₹{max_revenue}")