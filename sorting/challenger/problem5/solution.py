n = int(input())
L = list(map(int,input().split()))
for i in range(n):
    swapped = False
    for j in range(0 , n-i-1):
        if L[j] > L[j+1]:
            L[j] , L[j+1] = L[j+1] , L[j]
            swapped = True
    if not swapped:
        break
print(*L