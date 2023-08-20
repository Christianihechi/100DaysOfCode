student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_number = 0

for score in student_scores:
    if score > max_number:
        max_number = score
print(f"The highest_score in the class is: {max_number}")
