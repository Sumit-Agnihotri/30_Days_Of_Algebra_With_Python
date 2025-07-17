# Problem:
# Sumit's age is 5 more than twice his brother's age. If Sumit is 25, what is his brother's age?

age = int(input("Enter the age of the first person: "))
from sympy import symbols, Eq, solve

print("Let the age of the brother be x.")
x = symbols('x')
equation = Eq(2 * x + 5, age)
solution = solve(equation)
print(f"The age of the brother is: {solution[0]}")