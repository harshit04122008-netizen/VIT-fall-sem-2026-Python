import numpy as np
L = []
R = int(input())
C = int(input())
for _ in range(R):
    L.append(list(map(int,input().split())))
a = np.array(L)
print("Original array:\n",a)
expanded = np.expand_dims(a , axis = 1)
expanded = np.repeat(expanded , 2 , axis = 1)
print("Expanded array:\n",expanded)