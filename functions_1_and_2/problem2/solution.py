def calculate_gross_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate
def calculate_deductions(gross_salary):
    return 0.15*gross_salary
def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions
def print_salary_details(hours_worked, hourly_rate, monthly_salary):
    print(f"Hours Worked:{hours_worked:.2f} hours")
    print(f"Hourly Rate: {hourly_rate:.2f} per hour")
    print(f"Net Salary:{monthly_salary:.2f}")

hours_worked = float(input())
hourly_rate = float(input())

gross_salary = calculate_gross_salary(hours_worked, hourly_rate)
deductions = calculate_deductions(gross_salary)
monthly_salary = calculate_net_salary(gross_salary, deductions)

print_salary_details(hours_worked, hourly_rate, monthly_salary)