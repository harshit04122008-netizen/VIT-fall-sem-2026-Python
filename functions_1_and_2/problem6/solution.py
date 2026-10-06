DOMESTIC_RATE = 5.0
INTERNATIONAL_RATE = 10.0
REMOTE_RATE = 15.0
def calculate_shipping(weight, destination):
    if weight < 0 :
        print("Invalid weight. Weight must be greater than 0.")
        return None
    else:
        if destination == "Domestic":
            return DOMESTIC_RATE * weight
        elif destination == "International":
            return INTERNATIONAL_RATE * weight
        elif destination == "Remote":
            return REMOTE_RATE * weight
        else:
            print("Invalid destination.")
            return None
weight = float(input())
destination = input()
shipping_cost = calculate_shipping(weight, destination)
if shipping_cost is not None:
    print(f"Shipping cost to {destination} for a {weight} kg package: {shipping_cost:.2f}")