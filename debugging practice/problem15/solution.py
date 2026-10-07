def order_total(*prices, discount=0):
    total = sum(prices)
    total = total - (total * (discount/100) )
    return total

n = int(input())
prices = map(int, input().split())
discount = int(input())

if discount == 0:
    result = order_total(*prices)
else:
    result = order_total(*prices , discount = discount)

print(f"Order Total: {result:.1f}")