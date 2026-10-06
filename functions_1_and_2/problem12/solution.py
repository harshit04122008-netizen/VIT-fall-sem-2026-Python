is_alternating = lambda w: all((c in "aeiouAEIOU") != (w[i+1] in "aeiouAEIOU") for i ,c in enumerate(w[:-1]))
n = int(input().strip())
words = [input().strip() for _ in range(0,n)]
filtered_reversed = list(map(lambda w: w[::-1] , filter(is_alternating,words)))
result = sorted(filtered_reversed , key = lambda w: w[-1])
print(result)