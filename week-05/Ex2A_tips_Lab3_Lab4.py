# Lab 3 
# Input()
bank_bal = input("What is your current bank balance? ") 
print("Your balance is " + bank_bal)

#Example 1
# How much you want to tip?
tip = input("How much do you want to tip? ")
print("You want to tip " + tip) 

#The issue with the above code is that the input() can take any value, including non-numeric values.
# If the user enters a non-numeric value, it will cause an error when we try to perform calculations with it. 

#Lab 4
# F strings
total_due = 97
print("The total dues is " + str(total_due))
print(f"The total dues is {total_due}")

print(f"Food cost is {food_cost} and tax is {tax}")
print(f"The world population is {world_population} and the US population is {us_population}")


