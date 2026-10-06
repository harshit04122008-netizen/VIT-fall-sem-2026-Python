def analyze_string(input_string):
    test_string = input_string.strip()
    upper_case = 0
    lower_case = 0
    digits = 0
    special_char = 0
    for i in test_string:
        if i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1
        elif i.isdigit():
            digits += 1
        elif not i.isalnum():
            special_char += 1
    return upper_case ,lower_case ,digits ,special_char

input_string = input()
uppercase_count, lowercase_count, digit_count, special_count = analyze_string(input_string)

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Digits:", digit_count)
print("Special characters:", special_count)