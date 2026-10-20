import numpy as np
L = list(map(int,input().split()))
a = np.array(L)
np.sort(a)
print(f"Median Price: {np.median(a):.2f}")
print(f"Mean Price: {np.mean(a):.2f}")