# Welcome To Python (Game Version)

# This is going to be an introductory for the programming language Python and how to be better than everyone else!

# It'll compromise everything you would need to know about Python and how to tackle it

# Let's start! Hope you have fun :)

# Before we start if you're completely new to this then i would recommend using Pycharm as your IDE
# IDE = Integrated Development Environment (A software used to create other software!)

# You should also download the python software to make this work!

# Now let's actually start!

# By the way if you would like the videos I learnt this from i have attached it on my github
# (I guess you're looking at this from there!)

print("Hello!My friend")

print("This is going to be a wonderful journey Let's Start Learning! :0 ")

# This will be a game based story mode version!

# Beginner's Hut: Basics and Class Introductions

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

# Beginner's Hut: Mission 1

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

# Beginner's Hut: Skill Knowledge!

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

# Beginner's Hut: Communication and Setting Accommodations

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

# Beginner's Hut: Knowledge Absorption (Old Relic)

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

# Beginner's Hut: Dagger Skills

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
