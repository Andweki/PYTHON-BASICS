from email.mime import text


#name="Nicholas Kaguo"
#print(name)

input= input("enter your name: ")
print("Hello " + input)

age= 25
print("I am " + str(age) + " years old")

height=1.69
print("My height is " + str(height) + " meters")

is_student= True
print("I am a student? " + str(is_student))

class_name= "python programming"
print("I am taking a class called " + class_name.replace("python programming", "javascript programming").upper())

fruits=["Apple","Banana","Orange","Grapes","Watermelon"]
print(fruits)

fruits.append("Mango")
print(fruits)

fruits.remove("Grapes")
print(fruits)

print (len(fruits))
print(fruits)
