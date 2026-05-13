#math_and_stats

import random
import math
import statistics

#2. Create a few starting variables to work with:

vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

#Use a combination of functions from all three modules to create calculations that will support the following output 
# (and be sure to use comments to document your code as you work!):

#_Experimenting with a subset of integers 1-100:
#Sum of 75 sample values from 1 to 100: ____
print(sum(vals_sample)) 
#Average of 75 sample values: ____
 # print(statistics.average(vals_sample)) #I thought the function is average but it is not
print(statistics.mean(vals_sample))
#Median of 75 sample values: ____
print(statistics.median(vals_sample))

#_Experimenting with a superset of 200 values, integers 1-100:
#Average of 200 values: ____
print(statistics.mean(vals_choices))
#Median of 200 values: ____
print(statistics.median(vals_choices))
#Mode of 200 values: ____
print(statistics.mode(vals_choices))
#Standard deviation of 200 values: ____
print(statistics.stdev(vals_choices))
#Variance of 200 values: ____
print(statistics.variance(vals_choices))

#_Modeling a random circle:
#Radius = __, area = ____ (rounded up to the nearest integer)
#Radius = __, area = ____ (rounded down to the nearest integer)
area = pi*radius**2
print(area) # i used this to see the result before rounding up or down
print(math.ceil(area))
print(math.floor(area))

#a Final Statements
print(f"Experimenting with a subset of integers 1-100: \n\
      Sum of 75 sample values from 1 to 100: {sum(vals_sample)} \n\
    Average of 75 sample values: {(statistics.mean(vals_sample))} \n\
    Median of 75 sample values: {(statistics.median(vals_sample))} \n\
        Experimenting with a superset of 200 values, integers 1-100: \n\
    Average of 200 values: {(statistics.mean(vals_choices))} \n\
        Median of 200 values: {(statistics.median(vals_choices))} \n\
        Mode of 200 values: {(statistics.mode(vals_choices))} \n\
            Standard deviation of 200 values: {(statistics.stdev(vals_choices))} \n\
            Variance of 200 values: {(statistics.variance(vals_choices))} \n\
               Modeling a random circle: \n\
                   Radius = {(radius)}, area = {(math.ceil(area))} (rounded up to the nearest integer) \n\
                   Radius = {(radius)}, area = {(math.floor(area))} (rounded down to the nearest integer)")
#There was a space after the \n\ in line 56 i spent literally 20 minutes to find the issue in my script!!!

#c