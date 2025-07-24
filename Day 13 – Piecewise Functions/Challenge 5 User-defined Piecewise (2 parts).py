from sympy import symbols, Piecewise, sympify

x = symbols('x')
expr1 = sympify(input("Enter expression 1 (e.g., x**2): "))
cond1 = sympify(input("Enter condition 1 (e.g., x < 0): "))
expr2 = sympify(input("Enter expression 2 (e.g., x + 2): "))
cond2 = sympify(input("Enter condition 2 (e.g., x >= 0): "))

f = Piecewise((expr1, cond1), (expr2, cond2))
print("Piecewise function:")
print(f)

# Evaluate at some x values
for val in [-2, 0, 2]:
    print(f"f({val}) = {f.subs(x, val)}")