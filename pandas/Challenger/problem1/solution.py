import pandas as pd
L1 = []
L2 = []
for _ in range(4):
    L1.append(list(map(int,input().split())))
for _ in range(4):
    L2.append(list(map(int,input().split())))
L3 = []
for i in L1:
    L3.append({
        "A":int(i[0]),
        "B":int(i[1])
    })
df1 = pd.DataFrame(L3)
print("df1:")
print(df1)
L4 = []
for i in L2:
    L4.append({
        "A":int(i[0]),
        "B":int(i[1])
    })
df2 = pd.DataFrame(L4)
print("df2:")
print(df2)
print("After concatenating:")
res = pd.concat([df1,df2] , keys = ["key1" , "key2"])
print(res)