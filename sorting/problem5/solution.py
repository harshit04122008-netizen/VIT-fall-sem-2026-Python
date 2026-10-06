n = int(input())
L = list(map(int,input().split()))
max_value = int(input())
count = 0
for i in L:
    if i <= max_value:
        count += 1
print(count)
