""" f=open('test.txt',"x")
f.write("Hello!\nThis is my first file!")
f.close() """
""" 
f=open("test.txt", "r")
print(f.read())
f.close() """

""" with open("test.txt", "r") as f:
    print(f.read()) """
    
""" with open("test.txt" , "a") as f:
    f.write("\nThis is an addition") """
""" with open("test.txt", "r") as f:
    print(f.read())
     """
""" with open("test.txt", "a") as f:
    f.write("\nNew line added.")
     """
""" with open("test.txt","r") as f:
    print(f.read()) """
    
import csv

""" with open("sales_data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) """
        
""" 
data = [
    ['Product', 'Region', 'Amount'],
    ['Laptop', 'East', 1200.00],
    ['Phone', 'West', 850.00],
    ['Tablet', 'East', 400.00],
]

with open("sales_data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Dosya oluşturuldu!")
 """
 
""" with open("sales_data.csv","r") as f:
    reader = csv.reader(f)
   for row in reader:
        print(row)
    for row in reader:
        print(row[2])
        print(float(row[2])) """
        
""" with open("sales_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        #print(row[2])
        print(float(row[2])) """
    
""" with open("sales_data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        total = 0
        for row in reader:
            total += float(row[2])
print(f"Total sales: ${total:,.2f}") """


data = [
    ['Product', 'Region', 'Amount'],
    ['Laptop', 'East', 1200.00],
    ['Phone', 'West', 850.00],
    ['Tablet', 'East', 'UNKNOWN'],  # bad data
]

with open("sales_data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
with open("sales_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    total = 0
    for row in reader:
        try:
            total += float(row[2])
        except ValueError:
            print(f"{row[0]} için geçersiz değer: {row[2]}")

print(f"total sales: ${total:,.2f}")