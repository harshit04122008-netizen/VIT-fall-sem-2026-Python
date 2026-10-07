def calculate_bill(prices, quantity):
    return price * quantity


price = int(input())
quantity = int(input())

total = calculate_bill(price, quantity)

print("Total Bill:", total)