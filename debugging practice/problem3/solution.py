def binary_search(trains, query):
    left, right = 0, len(trains) - 1
    while left <= right:
        mid = (left + right) // 2
        if trains[mid] == query:
            return mid +1  
        elif trains[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    return -1
n = int(input().strip())
trains = list(map(int, input().strip().split()))
query = int(input().strip())
result = binary_search(trains, query)
print(result)