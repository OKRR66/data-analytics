#How do you calculate the distance between coordinates (x1, y1) and (x2, y2)? 
#Hint: You'll need to look up how to calculate a square root in Python, which may involve a function from the math module.

x1, y1 = input("Enter the coordinates of the first point (x1, y1) separated by a comma: ").split(',')
x2, y2 = input("Enter the coordinates of the second point (x2, y2) separated by a comma: ").split(',')
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(round(distance, 2))