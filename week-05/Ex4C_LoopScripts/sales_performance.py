#sales_performance

#2 You have been given the following list of sales records. Each record is a tuple containing a salesperson's name, their region, and their total sales for the month:

sales_data = [ ('Marcus Webb', 'East', 4250.00), 
              ('Priya Sharma', 'West', 5875.50),
              ('DeShawn Carter', 'East', 3100.75), 
              ('LaTonya Rivers', 'South', 6420.00), 
              ('Bob Nguyen', 'West', 4980.25), 
              ]

#3 Use a for loop to unpack each tuple directly in the loop statement, and print a summary line for each record that looks like this:
#for sales_person, region, total_sales in sales_data:
#    if total_sales > 5000:
#        print(f"{sales_person} ({region}) ${total_sales:,.2f}")
#4 Add a conditional inside your loop: if a salesperson's total is greater than $5,000, also print " ^ Top performer!" below their summary line
#for sales_person, region, total_sales in sales_data:
#    if total_sales > 5000:
#        print(f"{sales_person} ({region}) ${total_sales:,.2f}")
#        print("^ Top performer!")      
#    else:
#        print(f"{sales_person} ({region}) ${total_sales:,.2f}")
 #       
#5 BONUS: Add a variable before the loop to track total sales across all employees, and print the overall total after the loop finishes.

overall_sales = 0
for sales_person, region, total_sales in sales_data:
    overall_sales += total_sales
    if total_sales > 5000:
        print(f"{sales_person} ({region}) ${total_sales:,.2f}")
        print("^ Top performer!")  
    else:
        print(f"{sales_person} ({region}) ${total_sales:,.2f}")
        
print(f"Sales total is ${overall_sales}")