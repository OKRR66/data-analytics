#open_and_write.py

#Begin the script by creating a new variable to work with a file using the open function and including the append parameter, and create a new file named about_me.txt. Then close the file.
#a) Need a hint? For the variable, you can use the convention of naming it f. Refer to 4.A.2 and 4.A.4 for reference on the rest of the syntax to use.
""" f = open("about_me.txt", "a")
f.close() """

#4. Using Visual Studio Code (or Notepad if you prefer), open the new about_me.txt and add the following information: 
# (Note: If you prefer not to share information about yourself OR if you get a kick out of creative writing, feel free to make up a profile of a fictional person)
#a) Name:
#b) Place of birth: [be as general or specific as you want, e.g. “Tennessee” or “I was born in Australia, then my parents moved to the US when I was 3” are both good answers]
#c) Did you have any pets growing up? What kind? What were their names?
#d) If you could travel anywhere in the world for ONE WEEK, where would you go?
#e) If you could live anywhere in the world for a YEAR, where would you want to live?
""" f = open("about_me.txt", "a")
f.write("My name is Onur Karaer\n")
f.write("I was born in Yozgat/Turkiye\n")
f.write("I had a pet turtle when I was growing up. I named him Kaplumbaga.\n")
f.write("Japan is at the top of my bucket list. I want to see Tokyo, Okinawa and Kyoto.\n")
f.write("I would love to live in Brasil or Thailand for a year. I want that tropical warm weather!\n")
f.close() """

""" #I open it again in read mode to check my input
f.read()
#I learnt that to be able to read my file. I need to reopen it in read mode.
f = open("about_me.txt", "r")
print(f.read())
f.close() """
#I saw that it all came in one line so i added \n at the end of my inputs.
""" f = open("about_me.txt", "r")
print(f.read())
f.close() """
#Since i ran the code multiple times it appened the same text multiple times into my file.
#So i used w method to rewrite everything in a nice format.

""" f = open("about_me.txt", "w")
f.write("My name is Onur Karaer\n")
f.write("I was born in Yozgat/Turkiye\n")
f.write("I had a pet turtle when I was growing up. I named him Kaplumbaga.\n")
f.write("Japan is at the top of my bucket list. I want to see Tokyo, Okinawa and Kyoto.\n")
f.write("I would love to live in Brasil or Thailand for a year. I want that tropical warm weather!\n")
f.close()
f = open("about_me.txt", "r")
print(f.read())
f.close()

 """
#6) Update your script to add a new line, after opening the file, to use the .write() method to add the following additional information to the about_me.txt file:
a) If you could do anything for your "perfect" night out, where would you go and what would you do?
f = open("about_me.txt","w")
f.write("My perfect night would be in a nice boat in Istanbul Bosphorus with my wife, family and friends. Good food, music, and a great view.")
f.close()

f=open("about_me","r")
print(f.read())
f.close()

#Since i used w method it deleted previous content and added my answer to question 6 to file as expected.