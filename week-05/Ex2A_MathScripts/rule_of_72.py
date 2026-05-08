#rule_of_72
# How long will it take a savings account worth X to double in value based on an interest rate of IR? (Hint: Look up the “rule of 72”)
# The rule of 72 is a simple formula that estimates the number of years required to double an investment at a given annual rate of return. The formula is:
# Years to Double = 72 / Interest Rate
#a) Figure out the formula and what the script would look like, making up example values as needed.
savings = 1000
interest_rate = 0.05
years_to_double = 72 / (interest_rate * 100)

#b) Create the script in a file named rule_of_72.py

#c) The displayed output should be formatted as follows: Your current savings is [number]. 
# At a [number]% interest rate, your savings account will be worth [number] in [number] years
print(f"your current savings is {savings}."
      f" At a {interest_rate*100}% interest rate, your savings account will be worth "
      f"{savings*2} in {years_to_double} years.")


#d) Show your doubled balance with 2 digits to the right of the decimal point by using format(__, ".2f") 
# and show years with 1 digit to the right of the decimal. How can you do this using format()?
print(f"your current savings is {savings}."
      f" At a {interest_rate*100}% interest rate, your savings account will be worth "
      f"{format(savings*2, '.2f')} in {format(years_to_double, '.1f')} years.")
#e) There are a couple ways you might get the interest rate to display as a percentage. One option is to use the format function. 
# In this case, instead of including the character f to assign a fixed decimal format, use the character % to assign the percentage format, e.g. format(__, ".0%")
print(f"your current savings is {savings}."
      f" At a {format(interest_rate, '.0%')} interest rate, your savings account will be worth "
      f"{format(savings*2, '.2f')} in {format(years_to_double, '.1f')} years.")