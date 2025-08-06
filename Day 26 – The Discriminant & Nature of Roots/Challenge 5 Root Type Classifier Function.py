def root_type(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        return "Two real & distinct roots"
    elif D == 0:
        return "One real root (repeated)"
    else:
        return "Complex roots"

# Test
print(root_type(1, -2, 1))
print(root_type(1, 2, 5))
print(root_type(1, 5, 6))