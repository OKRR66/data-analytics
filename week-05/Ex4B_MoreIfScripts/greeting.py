# greeting
#Define a variable that contains the current hour (0-23). 
#Display one of the greeting below based on the current hour:
#Time Greeting until 10:00am Good morning! 10:00am until 5:00pm Good day! 5:00pm or later Good evening!
current_hour = int(input("Enter the current hour (0-23):  "))
if current_hour < 10:
    print("Good morning!")
elif current_hour < 17:
    print("Good day!")
else:
    print("Good evening!")
    
# The script above will saying "Good evening for any hour 17 or later, but we want it to say "Good evening!" only for hours 17-23. 
# Modify the script to check if the hour is between 17 and 23 (inclusive) before printing "Good evening!".
current_hour = int(input("Enter the current hour (0-23):  "))
if current_hour < 10:
    print("Good morning!")
elif current_hour < 17:
    print("Good day!")
elif 17 <= current_hour <= 23:
    print("Good evening!")
else:
    print("Invalid hour. Please enter a value between 0 and 23.")
    
#Update your script to include an additional condition that will print “What are you doing up so late??” if the hour is between 11pm and 4am.
current_hour = int(input("Enter the current hour (0-23):  "))
if  4 < current_hour < 10:
    print("Good morning!")
elif 10 <= current_hour < 17:
    print("Good day!")
elif 17 <= current_hour < 23:
    print("Good evening!")
elif current_hour >= 23 or current_hour <= 4:
    print("What are you doing up so late??")
else:
    print("Invalid hour. Please enter a value between 0 and 23.")
    