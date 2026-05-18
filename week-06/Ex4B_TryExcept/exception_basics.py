#exception_basics.py

# For each of the following exceptions, create a short code block that raises that exception. 
# Then put it within a try-except block to handle the error, an else block to print the result if no error occurs, and a finally statement like “Let’s try another one”:

#ValueError 
#NameError 
#TypeError 
#SyntaxError

try: 
    m = banana 
except NameError: 
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable") 
else: 
    print(m) 
finally: 
    print("Let's try another one...")