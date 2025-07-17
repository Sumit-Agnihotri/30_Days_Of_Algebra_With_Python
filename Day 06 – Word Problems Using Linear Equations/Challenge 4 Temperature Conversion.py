# Problem:
# Convert 98.6°F to Celsius using the formula.

fahrenheit
C = (F - 32) * 5/9
from sympy import symbols, solve, Eq
C, F = symbols('C F')
equation = Eq(C, (F - 32) * 5/9)
solution = solve(equation)
print(f"{F} is equal to {solution[0]}°C.")