ANNUAL_INTEREST_RATE = 7.0
loan_amount = float(input())
loan_duration = int(input())
def car_loan_installment(loan_amount, loan_duration):
    monthly_rate = (ANNUAL_INTEREST_RATE)/(12*100)
    total_months = loan_duration * 12
    numerator = loan_amount * monthly_rate * ((1+monthly_rate) ** total_months)
    denominator = ((1+monthly_rate) ** total_months) - 1
    return (numerator/denominator)
monthly_payment = car_loan_installment(loan_amount, loan_duration)

print(f"Monthly car instalment: {monthly_payment:.2f}")

