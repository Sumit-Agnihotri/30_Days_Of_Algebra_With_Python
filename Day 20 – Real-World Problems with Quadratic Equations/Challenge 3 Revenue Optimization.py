from sympy import symbols

x = symbols('x')

# Get user input: number of ₹10 price cuts
user_x = int(input("Enter number of ₹10 price cuts (x): "))

# Revenue function: R(x) = (200 - 10x)(100 + 5x)
revenue_expr = (200 - 10*x) * (100 + 5*x)

# Substitute the input value into the revenue function
revenue = revenue_expr.subs(x, user_x)

# Calculate the new selling price and units sold
price = 200 - 10 * user_x
units = 100 + 5 * user_x

print(f"\nIf ₹{10 * user_x} is reduced from price:")
print(f"➡️ Selling Price: ₹{price}")
print(f"➡️ Units Sold: {units}")
print(f"💰 Revenue: ₹{revenue}")