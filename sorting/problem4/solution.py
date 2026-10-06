n = int(input())
data = list(map(int,input().split()))
find = int(input())
i = data.count(find)
if i == 0:
    print(f"{find} Score not found.")
elif i == 1:
    print(f"{find} Score found only once.")
else:
    first_index = data.index(find)
    second_index = data.index(find , first_index+1)
    print(second_index)