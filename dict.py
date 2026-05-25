#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
#name/label-key:value
#Dictionaries are used to store data values in key:value pairs
student = {
    "name": "Nicholas Kaguo",  
    "age": 25,
    "course": "python programming",
}
print(student)  
#accessing dictionary items by key
#we use the key
print(student["course"]) #this will return the value associated with the key "course"

#adding items to a dictionary
student["school"]="lets code"
print(student)

#changing values in a dictionary
student["age"] = 26
print(student)

#removing items from a dictionary using pop() method specify key
student.pop("course") #this will remove the key "course" and its associated value from the dictionary
print(student)

#dictionary length using len() function
print(len(student)) #this will return the number of key:value pairs in the dictionary