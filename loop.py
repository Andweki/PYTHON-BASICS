#A loop is used to repeat a block of code multiple timees. In Python, there are two main types of loops: for loops and while loops.
#1. For Loops: A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. The syntax is:

for number in range(5):
    print(number)


#starting and ending range can be specified as well\
for number in range(12, 25):  
    print(number)

#Looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#break statement is used to exit the loop prematurely when a certain condition is met.
for x in range(10):
    if x == 5:
        break
    print(x)

#continue statement is used to skip the current iteration of the loop and move on to the next one.
for y in range(20):
    if y == 13:
        continue
    print(y)

#2. While Loops: A while loop is used to repeat a block of code as long as a certain condition is true.
count = 3
while count <= 25:
    print(count)
    count += 3  # This is equivalent to count = count + 1
    