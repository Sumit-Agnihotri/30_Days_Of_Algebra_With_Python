from sympy import symbols, solve_univariate_inequality, S

age = symbols('age')

# Step 1: Define inequality
inequality = age >= 17

# Step 2: Solve the inequality (get symbolic interval)
solution = solve_univariate_inequality(inequality, age, domain=S.Reals)
print("Eligible age range:", solution)

# Step 3: Check user's age
person_age = int(input("Enter your age: "))

# Use 'eval' to substitute and evaluate truth
is_eligible = inequality.subs(age, person_age)
print(f"Is person with age {person_age} eligible to vote? ➤", is_eligible)