n = int(input())
L = list(map(int,input().split()))
print("Given array")
print(*L)
for i in range(1,n):
    key = L[i]
    j = i - 1
    while j>=0 and L[j]>key:
        L[j+1] = L[j]
        j = j - 1
    L[j+1] = key
    print(f"After iteration {i}")
    print(*L)
print("Sorted Array")
print(*L)