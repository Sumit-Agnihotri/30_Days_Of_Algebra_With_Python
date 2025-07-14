from sympy import symbols, simplify

x, y = symbols('x y')
expression = 2 * x + 3 * y
value = expression.subs({x: 5, y: 10})
print("Evaluating the expression when x is 5 and y is 10 is:", value) # This should print 40.