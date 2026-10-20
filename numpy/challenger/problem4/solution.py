import numpy as np
L = []
R = int(input())
C = int(input())
for i in range(R):
    L.append(list(map(int,input().split())))
a = np.array(L)
print("Original 2D Array:\n",a)
D = []
for i in range(R):
    for j in range(C):
        if i == j:
            D.append(a[i,j])
print("Diagonal Slice:\n",np.array(D))