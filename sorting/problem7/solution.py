n = int(input())
L = list(map(int,input().split()))
for i in range(n):
    min_idx = i
    for j in range(i+1,n):
        if L[j] > L[min_idx]:
            min_idx = j
    L[i] , L[min_idx] = L[min_idx] , L[i]
for i in L[len(L)::-1]:
    print(i)