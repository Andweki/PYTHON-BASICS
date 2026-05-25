#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
#name/label-key:value
#Dictionaries are used to store data values in key:value pairs
student = (
    "name": "Nicholas Kaguo",  
    "age": 25,
    "course": "python programming",
)
print(student)  
#accessing dictionary items by key
#we use the key
print(student["course"]) #this will return the value associated with the key "course"

#adding items to a dictionary
student [:school] = "University of Nairobi" #this will add a new key "school" with the value "University of Nairobi" to the dictionary