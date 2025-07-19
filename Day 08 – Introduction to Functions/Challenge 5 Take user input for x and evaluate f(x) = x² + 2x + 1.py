from sympy import symbols, lambdify

x = symbols('x')
f = x ** 2 + 2 * x + 1
f_lambdified = lambdify(x, f)

user_input = int(input("Enter a value for x: "))
result = f_lambdified(user_input)
print(f"The result of f({user_input}) is: {result}")