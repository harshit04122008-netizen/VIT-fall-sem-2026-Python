import pandas as pd
L = list(map(int,input().split()))
I = {
    "0-100":[0,0],"101-200":[0,0],"201-300":[0,0],
    "301-400":[0,0],"400+":[0,0],"Total":[len(L),sum(L)]
}
for i in L:
    if 0 <= i <= 100:
        I["0-100"][0] += 1
        I["0-100"][1] += i
    elif 101<= i <= 200:
        I["101-200"][0] += 1
        I["101-200"][1] += i
    elif 201 <= i <= 300:
        I["201-300"][0] += 1
        I["201-300"][1] += i
    elif 301 <= i <= 400:
        I["301-400"][0] += 1
        I["301-400"][1] += i
    else:
        I["400+"][0] += 1
        I["400+"][1] += i
sol = []
for j in range(6):
    key , val = list(I.items())[j]
    if val[0] == 0:
        sol.append({
            "Interval":key,
            "Frequency":val[0],
            "Mean Consumption":"-"
        })
    else:
        sol.append({
            "Interval":key,
            "Frequency":val[0],
            "Mean Consumption":round(val[1]/val[0],2)
        })
df = pd.DataFrame(sol)
print("Electricity Consumption Summary")
print(df.to_string(index=False))
print(f"Overall Mean Consumption:{(I['Total'][1])/len(L)}kwh")
values = pd.Series(L)
print("Variance:",values.var())
print("Standard Deviation:",round(values.std(),2))