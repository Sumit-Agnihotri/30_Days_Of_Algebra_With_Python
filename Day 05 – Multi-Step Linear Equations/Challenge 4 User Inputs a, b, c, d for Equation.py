from sympy import symbols, Eq, solve, expand

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
d = int(input("Enter value for d: "))

x = symbols('x')

left = expand(a * (x + b) + c)
equation = Eq(left, d)
solution = solve(equation, x)

print(f"The solution for the equation {a} * (x + {b}) + {c} = {d} is: x = {solution[0]}")