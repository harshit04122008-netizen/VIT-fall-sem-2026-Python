import numpy as np
R , C = map(int,input().split())
L = []
for i in range(R):
    L.append(list(map(int,input().split())))
a = np.array(L)
print("sorted based on last axis(1):\n",np.sort(a))
b = a.flatten()
b.sort()
print("sorted flattened array:\n",b)
print("Sorted based on axis 0:\n",np.sort(a,axis = 0))