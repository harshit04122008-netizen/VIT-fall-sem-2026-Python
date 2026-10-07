def total_fee(base_fee, registration_fee=100):
    return base_fee + registration_fee


base_fee = int(input())
registration_fee = int(input())

if registration_fee > 0:
    result = total_fee(base_fee , registration_fee)
else:
    result = total_fee(base_fee)

print("Total Fee:", result)