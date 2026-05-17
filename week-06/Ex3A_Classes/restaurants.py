#restaurants.py

class Restaurant:
    
    def __init__(self,rest_name,food_type):
        self.rest_name = rest_name # restaurant name instance variable
        self.food_type = food_type # food type instance variable
        
    #3. Add two methods to the class:
    #a) The first method should be named describe_rest() and prints the output: [Restaurant name] serves [type of food].
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    #b) The second method should be named rest_open() and prints a simple message: [Restaurant name] is open.
    def rest_open(self):
        print(f"{self.rest_name} is open")
        
#44. Create three instances of the class for different types of restaurant. You can use the below examples or create your own:
restaurant1 = Restaurant("Wendy's", "Nasty burgers")
restaurant2 = Restaurant("Burger King", "Burgers that i would only eat if i was starving")
restaurant3 = Restaurant("Taco Bell", "Nasty but delicious food")


#5. Finally, call describe_rest() and rest_open() for each instance.
restaurant1.describe_rest()
restaurant1.rest_open()
restaurant2.describe_rest()
restaurant2.rest_open()
restaurant3.describe_rest()
restaurant3.rest_open()