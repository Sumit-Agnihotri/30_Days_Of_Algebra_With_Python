# Problem:
# A pencil costs ₹2 more than a pen. If 1 pencil and 1 pen cost ₹22 total, find the price of each.

print("Let the Pen price be x.")
from sympy import Eq, symbols, solve
x = symbols('x')

pencil_price = x + 2
pen_price = x
equation = Eq(pencil_price + pen_price, 22)
solution = solve(equation)
print(f"The price of the pen is ₹{solution[0]} and the price of the pencil is ₹{solution[0] + 2}.")