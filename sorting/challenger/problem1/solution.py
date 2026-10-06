n = int(input())
L = list(map(int,input().split()))
search = int(input())
count = 0
for i in range(n):
    if L[i] == search:
        print(f"Element {search} is present at index {i}")
        count += 1
if count == 0:
    print(f"Element {search} is not present in array")