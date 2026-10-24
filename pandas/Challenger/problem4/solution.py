import pandas as pd
L = list(map(int,input().split()))
I = {"Low (0-99)":0,"Moderate (100-199)":0,"High (200-299)":0,
    "Excellent (300+)":0
}
for i in L:
    if 0 <= i <= 99:
        I["Low (0-99)"] += 1
    elif 100 <= i <= 199:
        I["Moderate (100-199)"] += 1
    elif 200 <= i <= 299:
        I["High (200-299)"] += 1
    else:
        I["Excellent (300+)"] += 1
L1 = []
for key , value in I.items():
    L1.append({
        "Production Level":key,
        "Frequency":value
    })
print("Daily Production Analysis")
df = pd.DataFrame(L1)
print(df.to_string(index = False))
print("Average Production:" , (sum(L))/len(L))
values = pd.Series(L)
print(f"Variance: {round(values.var() , 2 )}")
print(f"Standard Deviation: {values.std():.2f}")