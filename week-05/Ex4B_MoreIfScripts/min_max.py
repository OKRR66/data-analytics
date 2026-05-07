#min_max
a= 1555
b= 3
c= 12312312
print(min(a,b,c))
print(max(a,b,c))

#Use ifelse statements to determine and display the answer
if a < b and a < c:
    print(f"The minimum is {a}")
elif b < c:
    print(f"The minimum is {b}")
else:
    print(f"The minimum is {c}")

if a > b and a > c:
    print(f"The maximum is {a}")
elif b > c:
    print(f"The maximum is {b}")
else:
    print(f"The maximum is {c}")