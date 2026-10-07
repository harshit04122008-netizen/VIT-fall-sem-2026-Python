def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n = int(input())
times = list(map(int, input().split()))

bubble_sort(times)

for x in times[::-1]:
    print(x, end=" ")