def digital_root(num):
    numbers = [int(digit) for digit in str(num)]
    digit_root = [int(digit) for digit in str(sum(numbers))]
    while len(digit_root) != 1:
        digit_root = [int(digit) for digit in str(sum(digit_root))]
    return digit_root[0]
num = int(input())
print(digital_root(num))