import numpy as np
R = int(input())
C = int(input())
L = list(map(int,input().split()))
a = np.array(L).reshape(R,C)
for i in range(R):
    for j in range(C):
        if i == j:
            a[i,j] = 0
print(a)