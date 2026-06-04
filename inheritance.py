#Inheritance 


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

account1 = Account("Dennis Maina", 40000)
account1.deposit(5000)

class SavingsAccount(Account):
    def earn_interest(self):
            print("Interest added to the account")
    def withdraw(self, amount):
            print("Withdawals are limited in a savings account")
  
savings_account1 = SavingsAccount("Brian", 5000)
savings_account1.deposit(5000)
savings_account1.withdraw(2000)
savings_account1.earn_interest()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = person("Alice", 20)
student1.show_info()

class Student(person):
    def __init__(self, name, age, marks, course,):
        super().__init__(name, age)
        self.marks = marks
        self.course = course

    def show_info(self):
        super().show_info()
        print(f"Marks: {self.marks}, Course: {self.course}")

    def study(self):
        print(f"{self.name} is studying {self.course}")

student2 = Student("Bob", 22, 85, "Computer Science")
student2.study()
