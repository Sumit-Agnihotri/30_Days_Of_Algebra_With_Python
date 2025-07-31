from sympy import symbols, Eq, solve

t = symbols('t')
h = -5*t**2 + 20*t

equation = Eq(h, 0)
times = solve(equation, t)
print("Time(s) when ball hits ground:", times)