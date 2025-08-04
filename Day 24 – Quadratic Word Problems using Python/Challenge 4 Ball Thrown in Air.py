from sympy import symbols, solve

t = symbols('t')
h = -5*t**2 + 20*t

# Vertex time = -b/(2a)
t_vertex = solve(h.diff(t))[0]
max_height = h.subs(t, t_vertex)
ground_hit = solve(h, t)

print("Time to max height:", t_vertex, "sec")
print("Max height:", max_height, "m")
print("Time to hit ground:", max(ground_hit), "sec")