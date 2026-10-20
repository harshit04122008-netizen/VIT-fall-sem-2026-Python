import numpy as np
n = int(input())
L = []
for i in range(n):
    string = input().split()
    L.append((string[0],int(string[1]),int(string[2])))
a = np.array(L , dtype = object)
sort_indices = np.argsort(a[:,2])
sorted_a = a[sort_indices]
print("[",end="")
for row in sorted_a:
    print(tuple(row),end=" ")
print("]")