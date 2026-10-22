import pandas as pd
n = int(input())
L = list(map(float,input().split()))
I = {"0-10":0,"11-20":0,"21-30":0,"31-40":0,"40+":0,"Total":len(L)}
for i in L:
    if 0<=i<=10:
        I["0-10"] += 1
    elif 11<=i<=20:
        I["11-20"] += 1
    elif 21<=i<=30:
        I["21-30"] += 1
    elif 31<=i<=40:
        I["31-40"] += 1
    else:
        I["40+"] += 1
sol = []
for i in range(len(I)):
    key , val = list(I.items())[i]
    sol.append({
        "Interval":key,
        "Frequency":val
    })
print("Frequency Distribution Table:")
df = pd.DataFrame(sol)
df.index = range(1,len(df)+1)
print(df)
values = pd.Series(L)
print(f"Mean Rainfall:{values.mean():.2f}")
print(f"Standard Deviation:{values.std():.5f}")