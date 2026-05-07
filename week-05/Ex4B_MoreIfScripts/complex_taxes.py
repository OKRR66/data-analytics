#complex_taxes

#1 Create a script named complex_taxes.py that will calculate federal tax based on the values of annual gross income (a number) and a filing status (‘single’ or ‘joint’).

#2 Start by copying your code for calculation of gross pay from the earlier lab (pay_rules.py) and include it here as part of your starting point. 
# Remember, that code calculates weekly gross pay. Extend that calculation to estimate annual gross pay (how many weeks in a year?) and save it to a new variable.

pay_rate = float(input("Enter the pay rate: "))
hours_worked = float(input("Enter the hours worked: "))
if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - regular_hours
    gross_pay = (regular_hours * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = hours_worked * pay_rate

annual_gross_pay = gross_pay * 52  # Assuming 52 weeks in a year

print(f"Annual gross pay: {annual_gross_pay:.2f}")

#3 Use a series of if statements to determine the appropriate tax rate. The tax table for single filers is:
# Annual Income Range     Tax Rate
# under 12,000             5%  
# 12,000 - 24,999.99       10%
# 25,000 - 74,999.99       15%
# 75,000 and over          20%

# The tax table for joint filers is:
# Annual Income Range     Tax Rate
# under 12,000             0%
# 12,000 - 24,999.99       10%
# 25,000 - 74,999.99       15%
# 75,000 and over          20%

filing_status = input("Enter filing status (single/joint): ")
if filing_status == 'single':
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif 12000 <= annual_gross_pay < 25000:
        tax_rate = 0.10
    elif 25000 <= annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == 'joint':
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif 12000 <= annual_gross_pay < 25000:
        tax_rate = 0.10
    elif 25000 <= annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

print(f"Tax rate: {tax_rate:.2f}")

#4 Use the tax rate to determine the tax withheld from the weekly gross pay.
weekly_tax_withheld = gross_pay * tax_rate
print(f"Weekly tax withheld: {weekly_tax_withheld:.2f}")

#5 Create separate print statements to print the relevant information determined by the above calculations.
#The output of your script might look something like this:
#You worked __ hours this period
#Because you earn $___ per hour, your gross weekly pay is $475 Your filing status is ___ Your tax withholding for the week is $___ Your net pay is $___

net_pay = gross_pay - weekly_tax_withheld
print(f"Net pay: {net_pay:.2f}")
print(f"You worked {hours_worked} hours this period")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${weekly_tax_withheld:.2f}")
print(f"Your net pay is ${net_pay:.2f}")

