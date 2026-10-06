def compress_string(input_string):
    elements = [letter for letter in input_string.strip()]
    unique_elements = []
    for i in elements:
        if i not in unique_elements:
            unique_elements.append(i)
    numbers = []
    for i in unique_elements:
        numbers.append(int(elements.count(i)))
    result =""
    for i in range(len(numbers)):
        if numbers[i] != 1:
            result += (unique_elements[i] + str(numbers[i]))
        else:
            result += unique_elements[i]
    return result

def main():
    input_string = input()
    print(compress_string(input_string))

if __name__ == "__main__":
    main() 