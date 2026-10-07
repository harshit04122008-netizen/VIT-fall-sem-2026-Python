def final_bill(*items, discount=0):
    total = 0

    for price, quantity in items:
        total += price * quantity

    total = total - (total * (discount / 100))

    return total

n = int(input())

items = []

for i in range(n):
    price, quantity = map(float, input().split())
    items.append((price , quantity))

discount = float(input())

result = final_bill(*items, discount=discount)

print(f"Final Bill Amount: {result:.1f}")