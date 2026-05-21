#a list is used to storre multiple items in a single variable
#Lists are written with square brackets[]

Students=["Nicholas","John","Jane","Mary"]
print(Students)

Marks=[85,90,78,92]
print(Marks)

#accessing list items by index
products=["Laptop","Phone","Tablet","Headphones"]
print(products[0]) #accessing the first item
print(products[1]) #accessing the second item
print(products[2]) #accessing the third item    

#negative indexing allows you to access list items from the end of the list
print(products[-1]) #accessing the last item
print(products[-2]) #accessing the second last item

#Changing list items
products[0]="Television"
print(products)

#adding items to a list using append() method
products.append("Speaker")
products.append("Camera")
products.append("Printer") #this will add the items to the end of the list
print(products)

#inserting items to a list using insert() method
products.insert(3,"Smartwatch") #this will insert the item at index 1
print(products)

#removing items from a list using remove() method specify item
products.remove("Tablet") #this will remove the item "Tablet" from the list
products.remove("Headphones") #this will remove the item "Headphones" from the list
print(products)

#.pop() method removes the last item from the list
products.pop() #this will remove the last item "Printer" from the list
print(products)

#checking the length of the list using len() function
print(len(products)) #this will return the number of items in the list  

#checking if an item exists in the list using in keyword
print("Laptop" in products) #this will return False because "Laptop" was changed to "Television"
print("Television" in products) #this will return True because "Television" is in the list

#NB a list can contain different data types
data=["Nicholas",25,True,3.14]
print(data)