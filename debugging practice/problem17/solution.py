def compute(base, **kwargs):
    square = base * base
    power_result = base ** kwargs["exponent"]
    return square, power_result

base = int(input())
exponent = int(input())

square, power_result = compute(base, exponent = exponent)

print("Square:", square)
print("Power Result:", power_result)