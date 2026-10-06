item_cost = float(input())
SALES_TAX_RATE = 0.08
def total_cost(item_cost):
    return item_cost + (item_cost * 0.08)

total_cost = total_cost(item_cost)
print(f"Item Cost: {item_cost:.2f}")
print(f"Sales Tax Rate: {SALES_TAX_RATE * 100}%")
print(f"Total Cost: {total_cost:.2f}")