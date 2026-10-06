def binary_to_decimal(binary_input):
    binary_str = binary_input.strip()
    if all(char in "01" for char in binary_str):
        return int(binary_str,2)
    else:
        return None

binary_input = input()
decimal_result = binary_to_decimal(binary_input)

if decimal_result is not None:
    print(f"The decimal equivalent of {binary_input} is {decimal_result}")
else:
    print("Invalid binary input. Please enter a valid binary number")