import numpy as np
n = int(input())
L = []
for i in range(n):
    L.append(int(input()))
a = np.array(L)
print("Original array:\n",a)
b = a[::-1]
print("Expanded array:")
print("[",np.concatenate((a,b)),"]")