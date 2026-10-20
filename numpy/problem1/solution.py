import numpy as np
R = int(input())
C = int(input())
L = []
for i in range(R):
    L.append((lambda i : [i*j for j in range(C)])(i))
print("Generated 2D Matrix:")
print(np.array(L))