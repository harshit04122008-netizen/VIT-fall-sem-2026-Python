n = int(input())
L = list(map(int,input().split()))
for i in range(1,n):
    key = L[i]
    j = i - 1
    while j >= 0 and key < L[j]:
        L[j+1] = L[j]
        j = j - 1
    L[j+1] = key
print(*L)