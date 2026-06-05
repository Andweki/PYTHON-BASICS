def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    greet("Nicholas")
    greet("welcome to python programming")
    
def add_numbers(a, b):
    print(a + b)

add_numbers(5, 10)

def square(number):
    return number * number

print(square(5))

#ATM system
class BankAccount:
    def __init__(self, account_name, balance):
        self.name = account_name   
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

account = BankAccount("Nicholas Kaguo", 1000)
print(account.name)
print(account.balance)
account.deposit(500)    
account.withdraw(200)

account1 = BankAccount("Alice", 10000)
print(account1.name)
print(account1.balance)
account1.deposit(5000)  
account1.withdraw(2500)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
       
    def start(self):
        print(f"{self.brand} is starting.")

Car1 = Vehicle("vehicle")
Car1.start()

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

Car2 = Car("Mercedes", "Gle")
Car2.drive()