def lis(arr,n):
    Sequence = []
    array = arr[n::-1]
    for i in range(n):
        if i == 0:
            if array[i] < array[i+1]:
                Sequence.append(array[i])
        if i == n-1:
            if array[i-1] < array[i]:
                Sequence.append(array[i])  
        elif array[i] < array[i+1] :
            Sequence.append(array[i+1])
    answer = []
    for i in Sequence:
        if i not in answer:
            answer.append(i)
    return len(answer) , answer

arr = list(map(int, input().split()))
length, subsequence = lis(arr, len(arr))
print(length)
print(subsequence)

