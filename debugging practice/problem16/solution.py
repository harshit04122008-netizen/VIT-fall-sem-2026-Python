def marks_summary(*marks):
    total = 0
    lowest = min(marks)

    for mark in marks:
        total = total + mark

        if mark < lowest:
            lowest = mark

    return total, lowest

n = int(input())
marks = map(float, input().split())

total, lowest = marks_summary(*marks)

print("Total Marks:", int(total))
print("Lowest Mark:", int(lowest))