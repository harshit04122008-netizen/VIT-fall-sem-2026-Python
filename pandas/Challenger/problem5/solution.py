import pandas as pd
n = int(input().strip())
user_ids = []
dates = []
for _ in range(n):
    line = input().strip()
    if line:
        user_id , date_str = line.split()
        user_ids.append(user_id)
        dates.append(date_str)
df = pd.DataFrame({
    "User_ID":user_ids,
    "Enrollment_Date":dates
})
df["dt"] = pd.to_datetime(df["Enrollment_Date"])
df["Day_of_Week"] = df["dt"].dt.day_name()
df["Half_Month"] = df["dt"].dt.day.apply(lambda day: "First" if day <= 15 else "Second")
df = df.drop(columns = ["dt"])
print("Processed:")
print(df)