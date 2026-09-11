n = int(input())
T1 = tuple(map(int,input().split()))

m = int(input())
T2 = tuple(map(int,input().split()))

T3 = ()

for i in T1:
    for j in T2:
        if i==j:
            if i not in T3:
                T3 += (i,)
                
print(T3)