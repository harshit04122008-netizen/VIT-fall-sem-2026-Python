n = int(input())

brand_units = {}
customer_spending = {}
brand_revenue = {}

for _ in range(n):
    name, brand, units, price = input().split()
    units = int(units)
    price = int(price)
    total_price = units * price

    if brand not in brand_units:
        brand_units[brand] = 0
    brand_units[brand] += units

    if name not in customer_spending:
        customer_spending[name] = 0
    customer_spending[name] += total_price

    if brand not in brand_revenue:
        brand_revenue[brand] = 0
    brand_revenue[brand] += total_price

max_brand = max(brand_revenue, key=brand_revenue.get)
top_brand = {max_brand:brand_revenue[max_brand]}

print(brand_units)
print(customer_spending)
print(top_brand)