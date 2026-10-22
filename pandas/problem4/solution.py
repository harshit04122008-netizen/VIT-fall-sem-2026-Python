import pandas as pd
L =[]
for _ in range(3):
    data = input().split()
    L.append({
        "Food Name":data[0],
        "Price": f"{float(data[1]):.2f}",
        "Quantity":int(data[2]),
        "Total Price":f"{float(data[1])*int(data[2]):.2f}"
    })
print(pd.DataFrame(L))