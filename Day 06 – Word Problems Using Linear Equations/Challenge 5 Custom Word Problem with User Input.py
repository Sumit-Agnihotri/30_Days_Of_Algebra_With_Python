# Problem:
# You spent ₹x on snacks and ₹10 on a drink. If your total bill was ₹50, how much did snacks cost?

drinks = int(input("Enter the cost of drinks (in ₹): "))
total_bill = int(input("Enter the total bill (in ₹): "))

from sympy import symbols, solve, Eq
x = symbols('x')
equation = Eq(x + drinks, total_bill)
solution = solve(equation)
print(f"The snacks cost ₹{solution[0]}.")