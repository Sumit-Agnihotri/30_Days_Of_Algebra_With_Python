age = int(input("Enter the age of the first person: "))
from sympy import symbols, Eq, solve

print("Let the second person's age be x.")
x = symbols('x')
equation = Eq(2 * x + 5, age)
solution = solve(equation)
print(f"The Second person's age is: {solution[0]}")