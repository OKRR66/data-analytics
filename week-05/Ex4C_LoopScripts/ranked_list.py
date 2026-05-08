#ranked_list

#2- Create a list of at least 5 items using anything you like: favorite foods, pets, cities you'd like to visit, skills you want to develop, etc.
Skills_to_develop = [
"SQL Queries",
"Story Telling",
"Python Coding",
"Financial Analysis",
"Public Speaking"]

#3 Use enumerate() with a for loop to print each item as a numbered list, starting at 1.

#for i, skill in enumerate(Skills_to_develop , 1):
#    print(f"{i} - {skill}")
    
    
#4 Now add an if statement inside your loop: if the index is 1 (i.e., the first item), also print " <- top pick!" on the same line.
#for i, skill in enumerate(Skills_to_develop , 1):
#    if i == 1:
#        print(f"{i} - {skill} <- top pick!")
#    else:
#      print(f"{i} - {skill}")
      
#5 BONUS: Modify your loop to print the list in reverse order (still numbered 1 through 5) using reversed() around your list.
for i, skill in enumerate(reversed(Skills_to_develop) , 1):
    if i == 1:
        print(f"{i} - {skill} <- top pick!")
    else:
        print(f"{i} - {skill}")
        
# Note to myself>> while reversing parenthesis should be around the list name. enumerate 1 is not taking a second argument!

