# Lesson 8

# "if" statements

# if statement = a block of code that'll execute if it's condition is true

age = int(input("What's your age?: "))

if age == 100:
    print("Your a century old!")
elif age >= 18:
    print("Congrats your a adult!")
elif age < 0:
    print("Alas, you haven't been born yet!")
else:
    print("You're a child!")

# Lesson 9

# Logical Operators (and, or, not)

temperature = int(input("What's the temperature outside?: "))

if temperature >= 0 and temperature <= 30:
    # You could simplify the above code by : if 0 <= temperature <= 30: That works too!
    print("The temperature is wonderful outside")
    print("Have fun outside! ")
elif temperature < 0 or temperature > 30:
    print("The condition outside is horrible today!")
    print("I would recommend not going outside!")

# We can also use the 'not' operator which reverse the condition!

# Lesson 10

# While Loops

# while loop = a statement that'll execute its block of code as long
# as it's condition remains true

### DANGEROUS CODE ###
# while 1==1:
#     name = print("Help! I'm stuck in a loop! ")

# Now let's look at a working example

name = ""

while len(name) == 0:
    name = input("Please Enter Your Name! ")

print("Hello, "+name)

# Another way of writing the example is

name = None

while not name:
    name = input("Please Enter Your Name! ")

print("Hello, " + name)

# Lesson 11

# 'for' loops

# It's a statement that'll execute a block of code for a limited amount of times

# While loops are unlimited
# for loops are limited

for i in range(10):
    print(i+1)

for i in range(50, 100+1, 2):
    print(i)

for i in "Blue_PegaCookie":
    print(i)

# We're gonna create a countdown timer!

import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year! ")

# Lesson 12

# Nested loops

# It's the inner loop that'll finish all of its iterations before finishing
# one iteration of da outer loop!

rows = int(input("How many rows would you like for the grid? "))
columns = int(input("How many columns would you like for the grid? "))
symbol = input("Please enter a symbol to create the grid with ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# Lesson 13

# Loop Control Statements

# It changes a loops execution from its normal sequence

# 1. Break = used to terminate the loop entirely
# 2. Continue = skips to the next iteration of da loop
# 3. Pass = does nothing, literally nothing. It acrs as a place holder

while True:
    name = input("What's your name? ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,20+1):
    if i == 13:
        pass
    else:
        print(i)

# Lesson 14

# Lists

# They're used to store multiple items in a single variable!

food = ["Pizza", "Hamburger", "Hotdog", "Spaghetti", "Dessert"]

food[0] = "Sushi"

print(food.append("Ice Cream"))
print(food.remove("Hotdog"))
print(food.pop())
print(food.insert(0, "Cake"))
print(food.sort())
print(food.clear())

for x in food:
    print(x)

# Lesson 15

# 2D Lists!

# It's a list of lists! How Fascinating!!!

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(drinks, dessert, dinner, sep="\n")
print(food, sep="\n")


# Lesson 16

# Tuples