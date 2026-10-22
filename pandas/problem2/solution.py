import pandas as pd
name = input()
age = int(input())
Qualification = input()
salary = float(input())
performance = input()
row = {
    "Name": name,
    "Age": age,
    "Qualification": Qualification,
    "Salary": salary,
    "Performance": performance
}
df = pd.DataFrame([row])
print(df)