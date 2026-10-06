n = int(input())
names = [input().strip() for _ in range(n)]
valid = list(filter(lambda x: len(x)>=4 , names))
if not valid:
    print("No valid strings")
else:
    new_name = list(map(lambda x: x[::-1].capitalize(),valid))
    for name in new_name:
        print(name)