# Welcome To Python (Game Version)

# I will be learning python (a programming language)

# It'll compromise everything you would need to know about Python and how to tackle it

# Let's start! Hope you have fun :)

# Before we start if you're completely new to this then I would recommend using Pycharm as your IDE
# IDE = Integrated Development Environment (A software used to create other software!)

# You should also download the python software to make this work!

# Now let's actually start!

# By the way if you would like the videos I learnt this from i have attached it on my github
# (I guess you're looking at this from there!)

print("Hello!My friend")

print("This is going to be a wonderful journey Let's Start Learning! :0 ")

# Lesson 1

# What's a Datatype? Mate Explain...

# Datatypes

datatype = "There are many datatypes which store data. The below are examples"

# Datatype: String
string = "This is a string (A series of characters) enclosed in ("") or ('')."

# Variable Store Datatypes
variable = "It is a container for a value. It behaves as the value it contains. It's not constant"

print(datatype)

# Name example

name = "Blue_PegaCookie"

# This prints the variable
print(name)

# This prints a string of text before the variable and we can add it
print("Hello, " + name)

# This prints the data type of the variable
print(type(name))

# Full name example

# Use a underscore to combine to words to make sense and make it a variable.
first_name = "Blue"

middle_name = "Pega"

last_name = "Cookie"

full_name = (first_name + "_" + middle_name + last_name)

print("Hello, " + full_name)

# Datatype: Integer
Integer = "A whole number i.e 1, 6, 9...."

# Age Example

age = 15

print(age)

print(type(age))

new_age = age + 1
# You could also do new_age += 1 (It's the same thing but better :)!

print(new_age)

# We usually use the datatype int to operate math operations in python not strings.

# error = print("Your age is: " + new_age)

# The above code wouldn't work as we can only use + to concatenate strings not integers

# Alternatively you can use

print(f"Your age is: {new_age} ")

# Or you can use

print("Your age is: " + str(new_age))
# The above code is also known as string casting

# Datatype: Float
# Floating point number! (Decimal Number)

Height = 274.93
print(Height)
print(type(Height))

print("Your height is: " + str(Height) + " cm")
# The above code is another example for string casting

# Datatype: Boolean

VariableT = True
print(VariableT)
print(type(VariableT))

VariableF = False
print(VariableF)
print(type(VariableF))

# Example for string casting

human = True
print("Are you a human? " + str(human))

# 4 basic Datatypes Have Been Covered
# 1. Strings
# 2. Integers
# 3. Floats
# 4. Booleans

# Lesson 2

# Multiple Assignments

# It allows us to assign multiple variables simultaneously in one line of code

name = "Blue_PegaCookie"
age = 15
Smart = True

print(name)
print(age)
print(Smart)

# Rather than using these many lines of code, We can use multiple assignments

name, age, smart = "Blue_PegaCookie", 15, True
# This looks compact and better and it produces the same results!

print(name)
print(age)
print(smart)

# Here's another example

Spongebob = 30
Squidward = 30
Ludwig = 30
Sandy = 30

# Instead of 4 lines of code Let's use multiple assignments

Spongebob = Squidward = Ludwig = Sandy = 30

print(Spongebob)
print(Squidward)
print(Sandy)
print(Ludwig)

# Lesson 3

# Useful String Methods

name = ("Blue_PegaCookie")

print(len(name))
print(name.find("z"))
print(name.capitalize())
print(name.upper())
print(name.lower())

# To find if string only contains number (no spaces also)
print(name.isdigit())

# To find if string only contains alphabets (no spaces also)
print(name.isalpha())

print(name.count("o"))
print(name.replace("_", "-"))
print(name * 5)

# Lesson 4

# All About Type Casting

# It's converting the datatype of a value to another datatype

# String
x = "1"

# Integer
y = 2

# Float
z = 4.35

Typecasting = 'To change the datatype of a variable, you have just got surround it by the daataype '

print(int(x))

# Lesson 5

# User Inputs

name = input("What's your name? ")

print("Hello, " + name)

age = input("How old are you? " + name)

x = int(age)
x += 1

print(f"Next year you'll be {x}")

# Alternatively you could choose to do this instead

name = input("What's your name? ")

print("Hello, " + name)

age = int(input("How old are you? " + name))

age += 1

print("Next year you'll be " + str(age))

# Lesson 6

# Mathematical Operations

import math

pi = 3.14

x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))

# Lesson 7

# String Slicing

# Slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Blue_PegaCookie"

first_name = name[0:4]  # Or [:4]
last_name = name[9:15]  # Or [9:]
print(first_name)
print(last_name)

messy_name = name[0:15:2]  # Or [::2]
print(messy_name)

reversed_name = name[::-1]
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slicer = slice(7, -4)

print(website1[slicer])
print(website2[slicer])

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

if 0 <= temperature <= 30:
    # You could simplify the above code by : if temperature >= 0 and temperature <= 30: That works too!
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

# Lesson 11

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

