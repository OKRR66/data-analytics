#savings_goal
#I commented out my scripts as i continue working on them to prevent confusions.
#2. Create a variable for your starting bank balance, another that sets your savings goal, and a third with your weekly savings amount.
starting_balance = 1000
savings_goal = 5000
weekly_savings = 200

#Use a while loop to compare your bank balance to your savings goal, if you haven’t met your goal yet, add the weekly savings amount to your bank balance. For each loop, print the statement, 
# “This week my balance increased to ___.” Once your savings goal is met, print the statement, “Goal met! My current balance is ___.”

#balance=starting_balance
#while balance < savings_goal:
#    balance += weekly_savings
#    print(f"This week my balance increased to ${balance}")
#print(f"Goal met! My current balance is ${balance}")

#4. Try adding additional logic to your loop:
#4a. If your balance is more than halfway to your goal, print the message, “Almost there! This week my balance is up to ___.”
#balance=starting_balance
#halfway = savings_goal / 2
#while balance < savings_goal:
#    balance += weekly_savings
#    if balance > halfway:
#        print(f"Almost there! This week my balance is up to ${balance}")
#    else:
#        print(f"This week my balance increased to ${balance}")
#    
#print(f"Goal met! My current balance is ${balance}")  # comment out the script on before running this one.

#4b If your balance is at least 75% of your goal, add a calculation to buy yourself a little treat. Print the message, “So close! After treating myself, my balance is up to ___.”
#treat = 150
#balance = starting_balance
#while balance < savings_goal:
#    balance += weekly_savings
#    if balance >= savings_goal *0.75:
#        balance = balance - treat
#        print(f"So close! After treating myself, my balance is up to ${balance}")
#    else: 
#        print(f"This week my balance increased to ${balance}")
    
#print(f"Goal met! My current balance is ${balance}") 

# IMPORTANT!!! IF YOU ENTER A TREAT AMOUNT >200 IT GOES TO AN INFINITE LOOP
# SO I ADD A SAFETY NET ON TOP AS BELOW
balance = starting_balance
treat = 30
if treat >= weekly_savings:
    print("Treat amount must be less than weekly savings. Exiting.")
else:
    balance = starting_balance
    while balance < savings_goal:
        balance += weekly_savings
        if balance >= savings_goal * 0.75:
            balance -= treat
            print(f"So close! After treating myself, my balance is up to ${balance}.")
        else:
            print(f"This week my balance increased to ${balance}.")
    print(f"Goal met! My current balance is ${balance}.")
    
    
    