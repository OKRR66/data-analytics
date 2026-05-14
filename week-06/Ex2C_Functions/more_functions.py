#more_functions

#The first should be named display_mailing_label(), 
# with five parameters: name, address, city, state and zip. 
# In the function output, format and display the data as you would on an address label.

def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(city + ", " + state + " " + zip)
    
#The second function should be named add_numbers() with one parameter defined to accept any number of arguments, 
# each argument being an integer. In the function, add given arguments together and display the result using the following format:
#number [+ number2 + number3 …] = result

def add_numbers(*args):
    result = sum(args)
    added = " + ".join(str(num) for num in args)
    print(f"[{added}] = {result}")
#add_numbers(1,2,3)

##I couldn't fully understand the question. I took help from Claude to get an explanation. I asked Claude to explain it in a pseudocode format. 
## Then I wrote the for loop to check all arguments that can be given. and I merged them into a strings to be able to use join.

#4 
def display_receipt(total_due, amount_paid):
    change_due = amount_paid - total_due
    if amount_paid >= total_due:
        print(f"Total Due: ${total_due:.2f}")
        print(f"Amount Paid: ${amount_paid:.2f}")
        print(f"Change Due: ${change_due:.2f}")
    else:
        print(f"Remaining balance to be paid: ${-change_due:.2f}")
#display_receipt(80, 60)


#5a
display_mailing_label("Onur Karaer", "1249 W Chase", "Chicago", "IL", "60626")
display_mailing_label("Jillian Furey", "123 E Maryland Ave", "Baltimore", "MD", "21201")

#5b
add_numbers(1)
add_numbers(4, 5)
add_numbers(1, 2, 3, 4, 5)

#5c
display_receipt(70, 100)
display_receipt(50, 50)
display_receipt(30, 20)

