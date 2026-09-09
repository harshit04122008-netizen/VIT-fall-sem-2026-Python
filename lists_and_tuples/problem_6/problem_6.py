n = int(input())
T = ()
for i in range(n):
    T_temp = tuple(input().split())
    T += (T_temp,)
y = int(input())
T_1 = T[y-1]
sums = 0
for s in range(12):
    sums += int(T_1[s])
print(format(sums/12,".2f"))