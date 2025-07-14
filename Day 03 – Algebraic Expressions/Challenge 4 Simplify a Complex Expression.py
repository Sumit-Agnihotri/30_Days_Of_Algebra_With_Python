from sympy import symbols, simplify

x = symbols('x')
expr = (2 * x + 4) / 2
simplified = simplify(expr)
print("Simplified form of (2x + 4)/2:", simplified) # Simplified form of (2x + 4)/2: x + 2