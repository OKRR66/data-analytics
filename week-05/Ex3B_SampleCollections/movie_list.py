# List of movies I watched
# The Lord of the Rings
# Matrix
# Pirates of the Caribbean: The Curse of the Black Pearl
# Dark Knight
# Godfather
# Shawshank Redemption
# Lion King
# Avengers
# Incredibles
# Finding Nemo

movie_list = [
    "The Lord of the Rings",
    "Matrix",
    "Pirates of the Caribbean: The Curse of the Black Pearl",
    "Dark Knight",
    "Godfather",
    "Shawshank Redemption",
    "Lion King",
    "Avengers",
    "Incredibles",
    "Finding Nemo"
]   
print(f"The list includes the {len(movie_list)} movies I'd like to watch")
print(movie_list)

# Print a sorted list two ways 
# Note: make sure that your list items aren't already in alphabetical order to start with, or you won't notice any difference

#a) Use the sorted() function to print a sorted list, then print the list again without using sorted()

print(sorted(movie_list))
print(movie_list)
#sorted() creates a brand new list, leaves the original untouched.

#b) use the .sort() method to sort the list, then print the list again

movie_list.sort()
print(movie_list)
#.sort changes the original list, it doesn't create a new one.

# 5)Think of at least one more movie to add to your list, and use the .append() method to add it. Then print the list again, also including an updated description statement.
movie_list.append("Inception")
print(movie_list)
print(f"The list now includes {len(movie_list)} movies I'd like to watch")

#6)Compare outputs with peers