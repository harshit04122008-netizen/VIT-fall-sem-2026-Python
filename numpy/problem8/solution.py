import numpy as np
L = list(map(int,input().split()))
a = np.array(L)
print("Original array:[",a,"]")
print("Expanded array (squared):",a**2)