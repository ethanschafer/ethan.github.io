# Create an empty list
myList = []
print ("Empty List")
print (myList)
print

# Create a list with stuff in it
print ("Lists with items in it")
coworkers = ["Sarah", "Matt", "Sophie"]
print (coworkers)

price = [32.23, 12.25, 56.38, 77.55, 39.0]
print (price)
print

# print the original list
print ("Changing item at index 1")
print (coworkers)

# change the item at index 1 
coworkers[1] = "Tim"
print (coworkers)
print

# Print the items in the list
print ("Items at index 0 and 2")
print (coworkers[0], coworkers[2])
print

myList = [2, 1, 31, 7, 5, 12, 8]

# Print the items in the list
print ("Using math to get items in a list")
print (myList[1 + 2])
print (myList[9 - 3])
print (myList[int(11 / 2)])

