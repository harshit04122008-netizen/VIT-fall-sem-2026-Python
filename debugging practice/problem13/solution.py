def final_price(item_price, delivery_charge):
    return item_price + delivery_charge


item_price = int(input())
delivery_charge = int(input())

result = final_price(item_price, delivery_charge )

print("Final Price:", result)