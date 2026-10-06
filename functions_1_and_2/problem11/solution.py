def harmonic_num(num):
    L = [int(digit) for digit in str(num).strip()]
    if 0 in L:
        return 0
    return len(L) / sum(1/d for d in L)
n = int(input())
num_list = [int(input()) for _ in range(n)]
threshold = float(input())
result = list(filter(lambda x: harmonic_num(x)>threshold,num_list))
print(result)