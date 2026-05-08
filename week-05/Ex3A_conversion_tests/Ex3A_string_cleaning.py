name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

#3- Use .lower() to convert all three names to lowercase and print each result.
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Use .title() to convert all three names to title case 
# (first letter of each word capitalized), and print each result. 
# (This is another useful method you can use alongside .upper() and .lower().)

print(name_1.title())
print(name_2.title())   
print(name_3.title())   

# Use .replace() to remove the $ from both salary strings, and print each result. 
# Add another print statement to test what data type these values are now. 
# What would you need to do next to perform math on them?
print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))
print(type(salary_1.replace("$", "")))
print(type(salary_2.replace("$", "")))
# To perform math on these values, you would need to convert them from strings to integers or floats.
# To convert to float we would remove both $ and , and then use the float/int function

# 6- Now chain .replace() and int() together in a single line to produce a usable integer from salary_1. Print the result and confirm its type using type().
print(int(salary_1.replace("$", "").replace(",", "")))  
print(int(salary_2.replace("$", "").replace(",", "")))  
print(type(int(salary_1.replace("$", "").replace(",", ""))))
print(type(int(salary_2.replace("$", "").replace(",", ""))))