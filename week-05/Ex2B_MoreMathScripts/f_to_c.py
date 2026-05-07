# Ex2B_MoreMathScripts

# 2. How do you convert a temperature from Fahrenheit to Celcius? 
# The formula is: C = (F - 32) / 1.8

fah = input("Please input temperature in Fahrenheit")
cel = (float(fah) - 32) / 1.8
print(f"{fah} degrees Fahrenheit is equal to {round(cel, 2)} degrees Celsius")



