from sympy import symbols, Abs, floor

x = symbols('x')
from sympy import Integer

functions = [
    ("Constant", Integer(5)),
    ("Identity", x),
    ("Linear", 2 * x + 3),
    ("Quadratic", x**2 - 4 * x + 3),
    ("Cubic", x**3),
    ("Absolute", Abs(x)),
    ("Step", floor(x))
]

for name, fx in functions:
    print(f"\n{name} Function:")
    for val in [-2, 0, 3]:
        result = fx.subs(x, val)
        print(f"  f({val}) = {result}")