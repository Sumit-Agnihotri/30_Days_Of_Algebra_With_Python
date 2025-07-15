from sympy import symbols, Eq, solve

x = symbols('x')
a = int(input("Enter the coefficient of x: "))
b = int(input("Enter the constant term: "))
c = int(input("Enter the constant term on the right side of the equation: "))

equation = Eq(a * x + b, c)
solution = solve(equation)
print(f"The solution to the equation {a}x + {b} = {c} is x = {solution[0]}")