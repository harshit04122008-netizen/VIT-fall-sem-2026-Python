import pandas as pd
from datetime import datetime
n = int(input())
L = []
for i in range(n):
    l = list(map(str,input().split()))
    user_id = l[0]
    time_stamp = l[1] + " " + l[2]
    L2 = l[2].split(":")
    hour = int(L2[0])
    date_obj = datetime.strptime(l[1],"%Y-%m-%d")
    is_weekend = date_obj.weekday() >= 5
    L.append({
        "User_ID":user_id,
        "Login_Timestamp":time_stamp,
        "Hour":hour,
        "Is_Weekend":is_weekend
    })
print("Processed:")
df = pd.DataFrame(L)
print(df)