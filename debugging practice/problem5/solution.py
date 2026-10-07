n = int(input())

students = {}

for _ in range(n):
    name = input()
    m = int(input())
    marks = list(map(int, input().split()))
    students[name] = marks

threshold = int(input())

qualified = []

for name, marks in students.items():
    total = sum(marks)
    print(f"{name}: {total}")

    if total >= threshold:
        qualified.append(name)

if qualified:
    print("Qualified:", *qualified)
else:
    print("Qualified: None")

