# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
score = int(input("Enter your score: "))
if score>100:
    print("check your score again.")
    exit()
grade = 'A' if score>=90 else 'B' if score>=80 else 'C' if score>=70 else 'D' if score>=60 else 'f'
print(f"Your score is {score} so you got: {grade} grade")