#sampling_tools
import random
products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

#4. For each of the following hypothetical scenarios, add the code to your script and run it to check the output before moving on to the next:

#a) The team wants to feature a "Product of the Day" based on one randomly selected item. Use random.choice() to select one product and print 
# the result with an appropriate label. Be sure to run the script a few times to confirm the selection changes with each run.
print(random.choice(products))
#b) Three products need to be selected for a brief usability survey. The same product should not appear more than once. 
# Use random.sample() to select 3 items from products without replacement and print the results.
print(random.sample(products, 3))

#c) For a presentation, all products should be displayed in a randomized order to avoid any appearance of ranking. Use random.shuffle() to shuffle the products list, then print the shuffled list. 
# Note: Unlike .choice() and .sample(), random.shuffle() does not return a shuffled list but rather modifies the list in place. Print products after shuffling, not the return value of 
# random.shuffle(), or you will get an output of None.
random.shuffle(products)
print(products)
#d) Use random.randint() to generate a simulated daily transaction count between 50 and 300, and print the result with a label.
print(f" {random.randint(50,300)} transactions occured for the product {random.choice(products)}.")
