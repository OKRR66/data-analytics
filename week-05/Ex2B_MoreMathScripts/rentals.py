# There are X people going on a tour. Charter vans seat 15 passengers each. 
# Vans cost $250 per day to rent (including the driver’s pay). 
# How many vans do you need? 
# How much will it cost to rent vans? 
# What is the cost if you split it per person?

number_of_people = int(input("Enter the number of people going on the tour: "))
vans_needed = (number_of_people + 14) // 15  # This ensures we round up to the nearest whole van
total_cost = vans_needed * 250
cost_per_person = total_cost / number_of_people if number_of_people > 0 else 0
print(f"You need {vans_needed} vans.")
print(f"The total cost to rent vans is {total_cost}.")
print(f"The cost per person is {cost_per_person:.2f}.")
# Results for 38 tourists
# a)How much money did your script say you had to charge per person?
# $19.74
# b) If you multiply that out, how much did you collect?
Collected = cost_per_person * number_of_people
print(f"Total collected from tourists: {Collected:.2f}")
# $750.00
# c) How much were the vans?
# $750.00
# d) Why do you have leftover money?
# I don't have leftover money. The total collected from tourists is equal to the total cost of renting the vans, which is $750.00. Because I rounded up the number of vans needed.
