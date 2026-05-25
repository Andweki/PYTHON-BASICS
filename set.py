#a set is a collection of unique items 
# that are unordered and unindexed. 
# Sets are defined using curly braces {} or the set() constructor. 
# Sets are mutable, meaning you can add or remove items from a set after it has been created. However, since sets are unordered, they do not support indexing or slicing like lists or tuples.
products = {"Laptop", "Phone", "Tablet", "Headphones", "Laptop"}
print(products) #this will print the set of products without duplicates

#adding items to a set using add() method
products.add("Speaker")
products.add("Camera")
print(products) #this will add the items to the set 

#use update() method to add multiple items to a set as a list
products.update(["Printer", "Smartwatch"])
print(products) #this will add the items to the set 

#removing items from a set using remove() method specify item
products.remove("Tablet") #this will remove the item "Tablet" from the set
print(products)
print(len(products)) #this will return the number of items in the set
