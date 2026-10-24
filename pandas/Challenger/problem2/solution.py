import pandas as pd
import numpy as np
n = int(input())
data = []
for _ in range(n):
    row = input().split()
    data.append(row)
columns = ["name" , "age" , "flight_id" , "state" , "rate"]
df = pd.DataFrame(data , columns = columns)
print(df)
df_updated = df.drop(columns = ["age" , "state"])
print(df_updated)
print(len(df_updated.columns))
print(np.array(df_updated.columns))