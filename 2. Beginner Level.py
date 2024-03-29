# Beginner's Hut: Mission 2

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

# Beginner's Hut: Mission 3

# Logical Operators (and, or, not)

temperature = int(input("What's the temperature outside?: "))

if 0 <= temperature <= 30:
    # You could simplify the above code by : if temperature >= 0 and temperature <= 30: That works too!
    print("The temperature is wonderful outside")
    print("Have fun outside! ")
elif temperature < 0 or temperature > 30:
    print("The condition outside is horrible today!")
    print("I would recommend not going outside!")

# We can also use the 'not' operator which reverse the condition!

# Beginner's Hut: Mission 4

# While Loops

# while loop = a statement that'll execute its block of code as long
# as it's condition remains true

# DANGEROUS CODE
# while 1==1:
#     name = print("Help! I'm stuck in a loop! ")

# Now let's look at a working example

name = ""

while len(name) == 0:
    name = input("Please Enter Your Name! ")

print("Hello, " + name)

# Another way of writing the example is

name = None

while not name:
    name = input("Please Enter Your Name! ")

print("Hello, " + name)

# Beginner's Hut: Final Spectrum

# 'for' loops

# It's a statement that'll execute a block of code for a limited amount of times

# While loops are unlimited
# for loops are limited

for i in range(10):
    print(i + 1)

for i in range(50, 100 + 1, 2):
    print(i)

for i in "Blue_PegaCookie":
    print(i)

# We're gonna create a countdown timer!

import time

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year! ")

# Beginner's Platoon: Knowledge Absorption

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

# Beginner's Platoon: Usage Of Knowledge

# Loop Control Statements

# It changes a loops execution from its normal sequence

# 1. Break = used to terminate the loop entirely
# 2. Continue = skips to the next iteration of da loop
# 3. Pass = does nothing, literally nothing. It acts as a place holder

while True:
    name = input("What's your name? ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 20 + 1):
    if i == 13:
        pass
    else:
        print(i)

# Venture Into The Forest: Enter

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

# Venture Into The Forest: Encounter

# 2D Lists!

# It's a list of lists! How Fascinating!!!

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(drinks, dessert, dinner, sep="\n")
print(food, sep="\n")

print(food[0])
print(food[0][1])
# the above code's first index chooses the first list in the variable food!
# the second index prints the item in the chosen list based on the number


# Lesson 16

# Tuples

# It's a collection  which is ordered and unchangeable
# It's used to group together related data

student1 = ("Blue_PegaCookie", 15, "male")
student2 = ("Marcel", 15, "male")
student3 = ("Daniel", 15, "female")
student4 = ("Joel", 15, "male")
student5 = ("Ava", 15, "female")
student6 = ("Roselin", 15, "female")

students = [student1, student2, student3, student4, student5, student6]



print(students.count("Blue_PegaCookie"))
print(student1.index("male"))

if "Blue_PegaCookie" in students:
    print("Blue_PegaCookie is present!")

# Lesson 17

# Sets

# It's a collection which is not in order and not indexed which also has not duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)

dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in dinner_table:
    print(x)

# Lesson 18

# Dictionaries

# It's a changeable, unordered collection of key:value pairs
# They're fast  because they use hashing
# It allows us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})
capitals.pop("China")
capitals.clear()

print(capitals["Russia"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key, value)
