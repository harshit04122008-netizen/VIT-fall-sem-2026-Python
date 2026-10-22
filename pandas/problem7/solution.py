import pandas as pd
I = {"Failing (0-49)":0,"Average (50-69)":0,
    "Good (70-89)":0,"Excellent (90-100)":0
}
L = list(map(int,input().split()))
for i in L:
    if 0<=i<=49:
        I["Failing (0-49)"] += 1
    elif 50<=i<=69:
        I["Average (50-69)"] += 1
    elif 70<=i<=89:
        I["Good (70-89)"] += 1
    else:
        I["Excellent (90-100)"] += 1
sol = []
for j in range(len(I)):
    key , val = list(I.items())[j]
    sol.append({
        "Performance Level":key,
        "Frequency":val
    })
df = pd.DataFrame(sol)
print("Student Performance Distribution")
print(df.to_string(index=False))