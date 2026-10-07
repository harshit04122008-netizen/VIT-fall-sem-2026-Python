def total_pay(salary, bonus):
    return salary + bonus

salary = int(input())
bonus = int(input())
total = total_pay(bonus=bonus , salary=salary)
print("Total Pay:", total)