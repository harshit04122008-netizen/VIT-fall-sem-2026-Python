emp1_salary = float(input())
emp2_salary = float(input())
emp3_salary = float(input())
emp4_salary = float(input())

salaries = (emp1_salary, emp2_salary, emp3_salary, emp4_salary)

difference = max(salaries) - min(salaries)

print("Difference:", f"{difference:.2f}")