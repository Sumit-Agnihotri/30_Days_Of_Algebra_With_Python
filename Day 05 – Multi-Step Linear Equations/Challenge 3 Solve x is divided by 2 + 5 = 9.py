from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq((x/2) + 5, 9)
solution = solve(equation, x)
print("The value of x is:", solution[0])