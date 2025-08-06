a, b, c = 1, -3, 2  # Change these to test different cases
D = b**2 - 4*a*c

print("Discriminant:", D)
if D > 0:
    print("✅ Two distinct real roots")
elif D == 0:
    print("✅ One real root (repeated)")
else:
    print("⚠️ Complex roots")