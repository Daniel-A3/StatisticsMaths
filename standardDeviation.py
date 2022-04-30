# Mean, Range, Variance and Standard Deviation in Python

from cmath import sqrt


dataSet = [1, 4, 2, 8, 4, 3, 5, 3, 11, 4, 13, 4]

def mean(dataSet):
    total = 0
    count = 0
    for i in dataSet:
        total += i
        count += 1
    dataMean = total / count
    return dataMean

def range():
    smallest = 999999
    biggest = 0
    for i in dataSet:
        if i > biggest:
            biggest = i
    for i in dataSet:
        if i < smallest:
            smallest = i
    return biggest - smallest

def variance():
    count = 0
    dataMean = mean(dataSet)
    difference = 0
    for i in dataSet:
        difference = difference + ((i - dataMean)*(i - dataMean))
        count += 1
    variance = difference / count
    return variance
    
def standardDeviation():
    return sqrt(variance())


print("The data set is : ") 
for i in dataSet:
    print(i, end=" ")
print("\nThe mean is : ", mean(dataSet))
print("The range is : ", range())
print("The variance is : ", variance())
print("The standard deviation is : ", standardDeviation())