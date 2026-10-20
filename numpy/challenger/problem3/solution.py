import numpy as np
n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))
a = np.array(L)
a_squeezed = np.squeeze(a)
fre_array_sorted = np.sort(a_squeezed)
fre_array_expanded = np.expand_dims(fre_array_sorted , axis = 0)
print("First Quartile (Q1):",np.percentile(fre_array_sorted , 25))
print("Second Quartile (Q2):",np.percentile(fre_array_sorted , 50))
print("Third Quartile (Q3):",np.percentile(fre_array_sorted , 75))