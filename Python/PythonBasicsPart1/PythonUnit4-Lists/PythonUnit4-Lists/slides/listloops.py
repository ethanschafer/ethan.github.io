import random

# Create an empty list
myList = []

# Add five random numbers between 10 and 50 to it
for num in range(5):
    myList.append(random.randint(10, 50))

print myList
print


# Create a list
myList = [21,16,12,27,36]

# Keep track of the sum
total = 0

for num in myList:
    # add item in list to total
    total += num

print "Sum of all numbers in", myList, "is:", 
print total


print "Numbers in myList"

myList = [56,65,98,2,25]

for num in myList:
    print num
