# pay_rules

#1 In a file named pay_rules.py, create a script to calculate gross pay given the
# variables pay_rate and hours_worked. If the person works more than 40 hours, pay the overtime hours at 1.5 times the rate of regular hours.
pay_rate = 17
hours_worked = 45
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - regular_hours
    gross_pay = (regular_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

print(f"Gross pay: {gross_pay:.2f}")

#3 Run your script several times with different values for pay_rate and hours_worked and confirm the output is right.
pay_rate = float(input("Enter the pay rate: "))
hours_worked = float(input("Enter the hours worked: "))
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - regular_hours
    gross_pay = (regular_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

print(f"Gross pay: {gross_pay:.2f}")