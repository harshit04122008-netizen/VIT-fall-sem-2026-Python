import pandas as pd
L = []
n = int(input())
for _ in range(n):
    L.append(input().split())
L1 = []
for i in L:
    L1.append({
        "Name":i[0],
        "Student ID":int(i[1]),
        "Department":i[2],
        "Age":int(i[3])
    })
print(pd.DataFrame(L1))