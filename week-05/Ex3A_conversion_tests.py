# Ex3A_conversion_tests.py
# Description: This script tests various numeric 
#               conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 " 
b = '55' 
c = "402 Stevens" 
d = 'Number 5 '

#5) For each variable, what happens when you try the following? Add comments to your script to document each result
#a) 
# int(a) # This will cause an error because the string contains a decimal point and cannot be converted to an integer.
int(b) # This will convert the string '55' to the integer 55.
# int(c) # This will cause an error because the string "402 Stevens" contains non-numeric characters and cannot be converted to an integer.
# int(d) # This will cause an error because the string 'Number 5 ' contains non-numeric characters and cannot be converted to an integer.

#b)
float(a) # This will convert the string " 101.1 " to the float
float(b) # This will convert the string '55' to the float 55.0.
# float(c) # This will cause an error because the string "402 Stevens" contains non-numeric characters and cannot be converted to a float.
# float(d) # This will cause an error because the string 'Number 5 ' contains non-numeric characters and cannot be converted to a float.

#c)
int(float(a)) # This will first convert the string " 101.1 " to the float 101.1, and then convert that float to the integer 101 by cutting the decimal part.

#d) Use slicing to add just the numeric portion of the string to a new variable (remember, indexing always starts with 0!),
# and cast the number as an integer or string, whichever is appropriate
e = d[7:8]  # This will extract the substring "5" from the string 'Number 5 '
f = int(e)  # This will convert the string "5" to the integer 5

#e) For variables a and d, use the .strip() method to remove the leading/trailing spaces, within a print statement to display each result.
print(a.strip())  # This will remove the leading and trailing spaces from the string " 101.1 " and print "101.1"
print(d.strip())  # This will remove the leading and trailing spaces from the string 'Number 5 ' and print "Number 5"


