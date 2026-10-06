from math import pow as power
def factors_and_count_digits(num):
    L = []
    for i in range(1,num+1):
        if num % i == 0:
            if i not in L:
                L.append(i)
            if i != num // i:
                if i not in L:
                    L.append(num//i)
    L.sort()
    print("Factors:", *L)
    number_list = [int(digit) for digit in str(num).strip()]
    print("Total digits:", len(number_list))

num = int(input())
factors_and_count_digits(num)