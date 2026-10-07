n = int(input())
items = list(input().split())  

duplicates = []
for item in items:
    if items.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

duplicates.sort()

print("Duplicate Items:", ' '.join(duplicates))