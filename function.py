#A function is a block of code that runs when called.
#Dry do not repeat yourself
def greet():
    print("Hello World!")


greet() #calling the function

#Function with parameters
def greet(name):
    print("Hello " + name + "!")

greet("Alice") #calling the function with an argument
greet("Bob") #calling the function with another argument 

#Function with multiple parameters
def add(a, b, c):
    print(a + b + c)

add(5, 10, 15)
add(10, 20, 30)

#function with return value
def price(amount, quantity):
    return amount * quantity

total_price = price(1000, 5)
print (total_price)

#functions + conditional statements
def check_age(number):  
    if number % 2 == 0:
        print("even number")
    else:
        print("odd number")
check_age(10)
check_age(15)

def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successful")   
    else:
        print("Invalid username or password")
login("admin", "1234")
login("user", "password")