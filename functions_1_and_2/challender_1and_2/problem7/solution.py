def unique_palindromic_substrings(s):
    unique_palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i+1,n+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                unique_palindromes.add(sub)
    return len(unique_palindromes)

s = input()
result = unique_palindromic_substrings(s)
print(result)