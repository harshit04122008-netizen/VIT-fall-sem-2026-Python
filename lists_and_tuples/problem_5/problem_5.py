n = int(input())
T = tuple(input().split())
r = int(input())
f = r - 1
T_2 = ()
for i in range(len(T)):
    if i in range(f,len(T),r):
        continue
    else:
        T_2 += (int(T[i]),)
print(T_2)

