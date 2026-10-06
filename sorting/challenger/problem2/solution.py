n = int(input())
L = list(map(int,input().split()))
even = []
odd = []
for i in range(n):
    if (i+1) % 2 == 0 :
        even.append(L[i])
    elif (i+1) % 2 != 0 :
        odd.append(L[i])
for i in range(1,len(even)):
    key = even[i]
    j = i - 1
    while j >= 0 and key < even[j]:
        even[j+1] = even[j]
        j = j - 1
    even[j+1] = key
for i in range(1,len(odd)):
    key = odd[i]
    j = i - 1
    while j >= 0 and key > odd[j]:
        odd[j+1] = odd[j]
        j = j - 1
    odd[j+1] = key
result = []
for i in range(max(len(odd),len(even))):
    if i < len(odd):
        result.append(odd[i])
    if i < len(even):
        result.append(even[i])
print(*result)