n = int(input())
L = list(map(int,input().split()))
for i in range(n):
    count = 0
    a = L[i]
    for j in range(i+1,n):
        if a >= L[j]:
            count += 1
    print(count , end =" ")