#dept_converter

#1 Write a script named dept_converter.py that uses if/elif/else logic to determine and print department name based on a department code. 
# Make sure to test your script with multiple codes. 
# 1 Marketing 
# 5 Human Resources 
# 10 Accounting 
# 12 Legal 
# 18 IT 
# 20 Customer Relations
dept_code = int(input("Enter the department code: "))
if dept_code == 1:
    print("Marketing")
elif dept_code == 5:
    print("Human Resources")
elif dept_code == 10:
    print("Accounting")
elif dept_code == 12:
    print("Legal")
elif dept_code == 18:
    print("IT")
elif dept_code == 20:
    print("Customer Relations")
else:
    print("Invalid department code.")
    
# Once your script is working, rewrite it using a match/case statement instead of if/elif/else. Save this version as dept_converter_v2.py

dept_code = int(input("Enter the department code: "))
match dept_code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Invalid department code.")