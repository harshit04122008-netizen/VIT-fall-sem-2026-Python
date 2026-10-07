def convert_to_inr(**donations):
    total = 0

    if "usd" in donations:
        total = total + donations["usd"] * 83

    if "eur" in donations:
        total = total + donations["eur"] * 90

    if "gbp" in donations:
        total = total + donations["gbp"] * 105

    return total


usd = float(input())
eur = int(input())
gbp = int(input())

result = convert_to_inr(usd=usd, eur=eur, gbp=gbp)

print("Total INR:", int(result))