n = int(input())
L = input().split()

L_1 = []

start = int(input())
end = int(input())

for i in range(end-1, start-2 ,-1):

    print(L[i], end=" ")
    L_1.append(int(L[i]))

print("\nMax:",max(L_1))

print("Min:",min(L_1))