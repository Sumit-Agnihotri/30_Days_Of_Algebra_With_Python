from sympy import Eq, symbols, solve, expand

x = symbols('x')

equation = Eq(expand(3 * (x - 2)) + 5, 20)
solution = solve(equation)
print(f"The solution to the equation is: x = {solution[0]}")