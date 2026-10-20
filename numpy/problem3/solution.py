import numpy as np
D = int(input())
L = list(map(int,input().split(" ")))
a = np.array(L)
new_shape = [1]*(D-1) + [len(L)]
a = a.reshape(new_shape)
print("Shape of the array:",a.shape)