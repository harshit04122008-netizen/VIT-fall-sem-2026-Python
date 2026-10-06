n = int(input())
words = [input().upper() for _ in range(n)]
reversed_words = list(filter(lambda x: x == x[::-1] , words))
sorted_words = sorted(reversed_words , key = lambda w: len(w),reverse =True)
if sorted_words:
    print(f"Length : {len(sorted_words[0])}")
else:
    print("Length: 0")
print(sorted_words)