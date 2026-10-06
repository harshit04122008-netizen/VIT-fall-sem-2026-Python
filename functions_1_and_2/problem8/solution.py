N = int(input())
def odd_numbers(N):
    List = []
    for i in range(N+1):
        if i % 2 != 0:
            List.append(i)
    return List
odd_number_seqence = odd_numbers(N)
print(*odd_number_seqence , sep = ", ")