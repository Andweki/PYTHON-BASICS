#Object oriented programming 
# (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. 
# It utilizes several techniques from previously established paradigms, including modularity, polymorphism, and encapsulation. 
# The main principles of OOP include:
# 1. Encapsulation: This principle is about bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class. It also restricts direct access to some of an object's components, which can prevent the accidental modification of data.
# 2. Inheritance: This allows a new class (called a child or subclass) to inherit attributes and methods from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes
# 3. Polymorphism: This principle allows objects of different classes to be treated as objects of a common superclass. It enables

# class -> blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
# object -> an instance of a class. It is a self-contained entity that consists of both

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

jeep=Car("Jeep", "Wrangler", 2023)
print(jeep.make)
print(jeep.model)
print(jeep.year)

toyota=Car("Toyota", "Corolla", 2022)
print(toyota.make)
print(toyota.model)
print(toyota.year)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} successfully deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} successfully withdrawn. New balance: {self.balance}")

account1 = Account("Jane Doe", 5000)
print(account1.owner)
account1.deposit(5000)
account1.withdraw(2000)

account2 = Account("John Doe", 20000)
print(account2.owner)
account2.deposit(10000)
account2.withdraw(8000)