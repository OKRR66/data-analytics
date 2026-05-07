#candy_store

#2. Start by creating two tuples: 
# one that lists at least 3 types of candy that can come in fruit flavors, 
# and another that lists at least 3 fruity flavors. (Feel free to get creative with your flavor ideas…)

candy_types = ("gummy bears", "sour worms", "fruit chews")
fruity_flavors = ("strawberry", "watermelon", "grape")

#3-Now create a new variable to store candy combinations as a set. 
# Using the index of each tuple, add at least one combination of each candy and flavor to the new set – 
# for example, putting together tuple1[0] and tuple2[1]
candy_combinations = set()
candy_combinations.add(candy_types[0] + " " + fruity_flavors[0])
candy_combinations.add(candy_types[1] + " " + fruity_flavors[1])
candy_combinations.add(candy_types[2] + " " + fruity_flavors[2])

#4-Create an output message that says, “Today’s candy options include:” and then prints the contents of the set.
print("Today's candy options include:")
print(candy_combinations)

#5-Print the output multiple times. What do you notice about the order of the items as you repeat the output?
print(candy_combinations)
print(candy_combinations)
print(candy_combinations)

#Since the set is not ordered, the order of the items may change each time you print it.
