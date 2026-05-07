# tiles
# You are going to tile a room whose dimensions are length by width feet. 
# There are twelve tiles per box, each 1 foot by 1 foot. 
# How many boxes of tiles do you need? You can only buy full boxes, not a partial box.
# You also want to buy at least 10% more tiles than you need in order to handle chips, breakage, and mess-ups. How many total boxes will you buy?

length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
area = length * width
tiles_needed = area
tiles_with_buffer = tiles_needed * 1.1
boxes_needed = -(-tiles_with_buffer // 12)  # This is a common way to round up in Python
print(f"You need to buy {int(boxes_needed)} boxes of tiles.")