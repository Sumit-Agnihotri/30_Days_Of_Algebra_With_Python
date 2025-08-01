from sympy import symbols, solve_univariate_inequality, S

score = symbols('score')
passing_score = 60

# Define the inequality
inequality = score >= passing_score

# Solve the inequality
solution = solve_univariate_inequality(inequality, score, domain=S.Reals)
print("Passing marks range:", solution)

# Check a specific score
student_score = int(input("Enter the student's score: "))
is_passed = inequality.subs(score, student_score)
print(f"Has the student with score {student_score} passed? ➤", is_passed)