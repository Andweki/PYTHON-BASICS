products = {"TV", "Laptop", "phone", "laptop"}
print(products)

devices = set()
devices.add("Keyboard")
devices.update(["Mouse", "speaker"])
print(devices)

product = {
    "name": "Laptop",
    "price": 1200,
    "brand": "Dell",       
}
product["price"] = 1000

product["stock"] = 50
print(product)

age = int(input("Enter your age: "))
if age >= 18:
    print("Adult.")
else:
    print("Minor.")

Marks = int(input("Enter your marks: "))
if Marks >= 80: 
    print("Grade A")
elif Marks >= 60:
    print("Grade B")    
else:
    print("Grade C")

for number in range(10):
    if number == 3:
        continue
    if number == 8:
        break
    print(number)


