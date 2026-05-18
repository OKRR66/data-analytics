#restaurants.py

class Restaurant:
    
    def __init__(self,rest_name,food_type):
        self.rest_name = rest_name # restaurant name instance variable
        self.food_type = food_type # food type instance variable
        self.number_served = 0 # number served instance variable, default value is 0
        self.customer_rating = [] # Customer ratings instance started as an empty list.
        
    #3. Add two methods to the class:
    #a) The first method should be named describe_rest() and prints the output: [Restaurant name] serves [type of food].
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    #b) The second method should be named rest_open() and prints a simple message: [Restaurant name] is open.
    def rest_open(self):
        print(f"{self.rest_name} is open")
        
    #3Add a method called add_num_served() that accepts an input for “How many customers served today?” and adds that amount to the self.number_served attribute.
    def add_num_served(self):
        served = int(input(f"How many customers served today?: "))
        self.number_served += served
        print(f"{self.rest_name} served {self.number_served} customers in total.")
        
    #4. Add a method called print_num_served() that prints the output: [Restaurant name] has served [number] customers
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")
        
    #5. Add a method for customer_rating() that accepts an input of integers 1-5 for 
    # “How would you rate your experience today on a scale of 1-5 (5 being excellent)?” 
    # Add that number to the list of self.customer_ratings, and print the statement “Your rating was ___.
    # The average rating for this restaurant is ___” (You can calculate the average using the sum of the ratings list, divided by the list length.)
    def customer_ratings(self): #I changed the name of this method, i added an s at the end to prevent errors. Because there is a class attribute with same name.
        rating = int(input(f"How would you rate your experience roday on a scale of 1-5 (5 being excellent)?: "))
        if rating >= 1 and rating <= 5:
            self.customer_rating.append(rating)
            average_rating = sum(i for i in self.customer_rating) / len(self.customer_rating)
            print(f"Your rating was {rating}. The average rating for this restaurant is {average_rating}.")
        else:
            print("Your rating must be between 1-5")
  
    
#44. Create three instances of the class for different types of restaurant. You can use the below examples or create your own:
restaurant1 = Restaurant("Wendy's", "Nasty burgers")
restaurant2 = Restaurant("Burger King", "Burgers that i would only eat if i was starving")
restaurant3 = Restaurant("Taco Bell", "Nasty but delicious food")


#5. Finally, call describe_rest() and rest_open() for each instance.
#restaurant1.describe_rest()
#restaurant1.rest_open()
#restaurant2.describe_rest()
#restaurant2.rest_open()
#restaurant3.describe_rest()
#restaurant3.rest_open()
#restaurant1.add_num_served()
#print(f"{restaurant1.rest_name} served {restaurant1.number_served} customers")
""" restaurant1.customer_ratings()
restaurant1.customer_ratings()
print(restaurant1.customer_rating)  # checking the list
restaurant1.customer_ratings()
print(restaurant1.customer_rating) """  # if i write the same script multiple times in one run i can see average is updating but if i write it once and run multiple time average is not changing????

#6. Test your new methods:
#a) For each of your example restaurants, run print_num_served() to check the initial value. 
# Then run add_num_served() a few times, inputting different values. Finally, run print_num_served() again to check the updated balance.
""" restaurant1.print_num_served()
restaurant1.add_num_served()
restaurant1.add_num_served()
restaurant1.print_num_served()

restaurant2.print_num_served()
restaurant2.add_num_served()
restaurant2.add_num_served()
restaurant2.print_num_served()

restaurant3.print_num_served()
restaurant3.add_num_served()
restaurant3.add_num_served()
restaurant3.print_num_served() """
#b) For each of your example restaurants, run customer_rating() several times, inputting a 
# different rating each time. Confirm that the average rating updates appropriately each time.
restaurant1.customer_ratings() # I noticed that average is not updating if i don't run it multiple times before this question. I added my notes regarding this situation above.
restaurant1.customer_ratings()
restaurant1.customer_ratings()

restaurant2.customer_ratings()
restaurant2.customer_ratings()
restaurant2.customer_ratings()

restaurant3.customer_ratings()
restaurant3.customer_ratings()
restaurant3.customer_ratings()
#c) For customer_rating(), try inputting a few “incorrect” values, like the number 6, 
# a decimal number such as 2.5, and a word/phrase such as “5 stars!”. Does your

restaurant1.customer_ratings() 
