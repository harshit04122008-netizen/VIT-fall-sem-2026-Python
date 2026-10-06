side1 = float(input())
side2 = float(input())
def calculate_hypotenuse(side1, side2):
    return ((side1)**2 + (side2)**2)**0.5

result = calculate_hypotenuse(side1, side2)
print(f"The length of the hypotenuse is: {result:.2f}")