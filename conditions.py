#conditional statements allow your program to make decisions based on certain conditions. The most common conditional statements in Python are if, elif, and else.
#the IF statement runs only when a certain condition is true. If the condition is false, the code block inside the if statement will be skipped.
age = 18    

if age >= 18:
    print("You are an adult you can vote.")

#the ELSE statement runs when the condition in the if statement is false.
score = 60      

if score >= 50:
    print("Pass.")

else:
    print("Fail.")

amount=2000
if amount >= 3000:    
    print("Eligible for 20% discount.")
else:
    print("Not eligible for 20% discount.")

#the ELIF statement allows you to check multiple conditions.
marks = 81
if marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:           
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Fail")

#Multiple conditions (and, or)
#and operator returns true if both conditions are true
client_age = 25 
has_id = True

if client_age >= 18 and has_id:
    print("Access granted.")

#or operator returns true if at least one condition is true 
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Weekend!")
    

