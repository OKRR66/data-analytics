# c_to_f

#2. How do you convert a temperature from Celsius to Fahrenheit?
# The formula is: F = (C * 9/5) + 32

cel = input("Enter a temperature in Celsius: ") 
fah = (float(cel) * 9/5) + 32
print(f"{cel} degrees Celsius is equal to {fah} degrees Fahrenheit.")
