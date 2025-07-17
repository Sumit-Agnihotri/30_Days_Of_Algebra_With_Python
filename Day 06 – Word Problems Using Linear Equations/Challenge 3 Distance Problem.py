# Problem:
# A car travels at 60 km/h. How far does it travel in x hours if it went 180 km?

distance_to_travel = int(input("Enter the distance to travel in km: "))
print("Let the time in hours be x.")
from sympy import Eq, symbols, solve

x = symbols('x')
equation = Eq(60 * x, distance_to_travel)
solution = solve(equation)
print(f"The car travels {solution[0]} hours to cover {distance_to_travel} km.")