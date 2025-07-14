from sympy import symbols, simplify

x = symbols('x')
expr = 3 * x + 2 * x - x
result = simplify(expr)
print("Combining like terms in 3x + 2x - x:", result) # Output: 4*x