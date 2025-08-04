from sympy import symbols, simplify, solve

x = symbols('x')

# Correct expressions
price = 100 - 10*x
people = 200 + 20*x

# Total Revenue = price * people
revenue = simplify(price * people)
print("Revenue equation:", revenue)

# Derivative to maximize
revenue_derivative = revenue.diff(x)
optimal_x = solve(revenue_derivative)[0]
max_revenue = revenue.subs(x, optimal_x)

print(f"Best ₹10 cuts: {optimal_x}")
print(f"Max Revenue: ₹{max_revenue}")