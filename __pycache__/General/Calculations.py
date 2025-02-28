import numpy
import matplotlib.pyplot as plt

# Calculate the average speed of 13 cars as recorded in the list below
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print("The average speed is: " , x)

print("-----------------------------")

# Calculate the median speed of 13 cars as recorded in the list below
x = numpy.std(speed)

print("The standard deviation is: ", x)

print("-----------------------------")

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# Calculate the 75th percentile 
x = numpy.percentile(ages, 75)

print("Percentile : ", x)



