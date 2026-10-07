n = int(input())
codes = list(map(int, input().split()))

duplicates = ()
for code in codes:
    if codes.count(code) > 1 and code not in duplicates:
        duplicates += (code,)

if duplicates:
    print("Duplicates:", ' '.join(map(str, duplicates)))
else:
    print("No duplicates found")

