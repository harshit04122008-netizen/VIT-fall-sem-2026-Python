import pandas as pd
L = []
for _ in range(5):
    info = input().split()
    name = info[0]
    age = int(info[1])
    city = info[2]
    qualification = info[3]
    marks = list(map(int,input().split()))
    avg_marks = sum(marks)/len(marks)
    L.append({
        "Name":name,
        "Age":age,
        "City":city,
        "Qualification":qualification,
        "Average Mark":f"{avg_marks:.2f}"
    })
df = pd.DataFrame(L)
print(df)