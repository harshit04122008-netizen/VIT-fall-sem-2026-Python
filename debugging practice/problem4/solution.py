n = int(input())
students = []

for i in range(n):
    data = input().split()
    name = data[0]
    math = int(data[1])
    science = int(data[2])
    english = int(data[3])
    student_record = (name, (math, science, english))
    students.append(student_record)

for student in students:
    name, marks = student
    total = sum(marks)
    average = total / 3
    print(f"{name} has average {average:.2f}")