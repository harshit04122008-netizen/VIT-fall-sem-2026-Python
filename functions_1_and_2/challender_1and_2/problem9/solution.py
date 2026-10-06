import math
n = int(input())
L = list(map(int,input().split()))
L1 = list(map(lambda i: math.prod(L[:i] + L[i+1:]),range(len(L))))
L2 = list(map(lambda i: math.prod(L[:i+1]),range(len(L))))
print("Product except current:",L1)
print("Prefix Products:",L2)

