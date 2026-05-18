#open_and_read.py

#10 Now, create a new script named open_and_read.py that includes the following steps:
#a) Open the file about_me.txt in read mode.
f = open(r"C:\Users\onurkaraer\Documents\DataAnalytics\week-06\Ex4A_ReadWriteFiles\about_me.txt", "r") # Since my vscode is working in a different directory i had to use the path of my file
#b) Print the contents of the file to the terminal using .read().
""" print(f.read(50)) #Q12> When i added 50 parameter i only see the first 50 character of my file.
 """
""" #c) Close the file
f.close() """

""" #reads only the first 10 characters
print(f.readline(10))
print(f.readline())
for i in range(1, 5):
    print(f.readline())
     """
    
""" #Now comment out the line using .readline(), and try experimenting with the .readlines() method:
#a) What do you get when you print using .readlines(1) with no argument specified?
print(f.readlines(1)) #I printed the first line but it appeared like a list element between brackets.
#b) Add another print statement using .readlines(1) – what do you get?
print(f.readlines(1)) # It gave the next line to read. So I am assumung readlines gives the next line we haven't printed yet. """
""" #c) Add a print statement using .readlines(10) – what do you get?
print(f.readlines(10)) # This line just gave the 3rd line.(Next first line we haven't printed yet) I would expect it to give next 10 lines we haven't seen.

#d) Add another print statement using .readlines(10), and commend out the first two print statements using .readlines(1) – now what do you get?
print(f.readlines(10)) # I only got first two lines of my text. """

#e) What do you get with .readlines(100)? How about .readlines(-1)?
""" print(f.readlines(100)) # This gave all the lines in a list format.
 """
""" print(f.readlines(-1)) #This also gave all the lines in a list format
 """
 
#Let’s try combining different types of read methods. First comment out all the print statements in your script. Then add three new variables with the following:
#a) One variable using .read(50)
first_50 = f.read(50)
print("read(50)>>: ")
print(first_50)

#b) A variable to capture the output of a loop using .readline() – you’ll need to update the loop logic to append to the new list rather than print
readline_list = []
for i in range(1, 5):
    readline_list.append(f.readline())
print("readline() loop output>")
print(readline_list)
#c) A variable using .readlines(100)

remaining_lines = f.readlines(100)
print("readlines(100)>")
print(remaining_lines) ## Since my text is short the loop covered all the texts and no remaning chracters to be showned in this line

f.close()