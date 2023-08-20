student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

number_of_students = 0
sum_of_heights = 0

for student in student_heights:
    number_of_students += 1

for height in student_heights:
    sum_of_heights += height

average_height = round(sum_of_heights / number_of_students)
print(f"Number of students: {number_of_students}")
print(f"Average_height: {average_height}")
