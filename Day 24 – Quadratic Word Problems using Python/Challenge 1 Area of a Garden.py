from sympy import symbols, Eq, solve

w = symbols('w')  # width
l = w + 5          # length
perimeter = 2*l + 2*w

eq = Eq(perimeter, 60)
solution = solve(eq, w)
w_val = solution[0]
l_val = w_val + 5
area = l_val * w_val

print(f"Width: {w_val} m, Length: {l_val} m, Area: {area} sq.m")