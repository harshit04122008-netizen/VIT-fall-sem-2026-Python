weight = float(input())
height = float(input())

def calculate_bmi(weight, height):
    return format(weight/(height)**2,".2f")

bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)