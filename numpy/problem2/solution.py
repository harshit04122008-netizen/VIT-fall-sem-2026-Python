import numpy as np
R = int(input())
C = int(input())
a = np.ones((R,C))
for i in range(R):
    for j in range(C):
        if i % 2 == 0 and j % 2 != 0 or i % 2 != 0 and j % 2 == 0:
            a[i,j] = 0
print(a)