student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

min_score = student_scores[0]

for score in student_scores:
    if score < min_score:
        min_score = score
print(f"The lowest score is: {min_score}")
