def count_vowels(input_string):
    count = 0
    for a in input_string:
        if a in "aeiouAEIOU":
            count+=1
    return count
input_string = input()

vowel_count = count_vowels(input_string)

print(f"Number of vowels in the string: {vowel_count}")