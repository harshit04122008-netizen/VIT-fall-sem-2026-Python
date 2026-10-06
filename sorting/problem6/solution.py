n = int(input())
L = list(map(int,input().split()))
max_value = int(input())
diff = []
value = []
for i in L:
    if i<=max_value:
        difference = max_value - i
        diff.append(difference)
        value.append(i)
if len(diff) == 0:
    print(f"No closestitem with an ID less than or equal to {max_value} exists in the warehouse")
else:
    min_index = diff.index(min(diff))
    print(f"The closest item ID less than or equal to {max_value} is {value[min_index]}")