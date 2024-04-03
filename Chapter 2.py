# Lesson 19

# Indexing

# Index Operator [] = Gives Access To A Sequence's Element (str, list, tuples)

name = "blue_PegaCookie"

if name[0].islower():
    name = name.capitalize()
print(name)

first_name = name[:4].upper()
print(first_name)

last_name = name[9:].lower()
print(last_name)

last_character = name[-1]
print(last_character)


# Lesson 20

# Functions = A block of code executed when called for

def I_dont_know_what_function():
    pass


def Hello():
    print("Hello!")


Hello()


def GoodDay():
    print("Hey!")
    print("Have a good day ahead!")


GoodDay()
GoodDay()
GoodDay()


def Function(new_name):
    print(f"Hey Man, Your name is {new_name} right?")
    print("Well... Welcome!")


newbie_name = "Blue_PegaCookie"

Function(newbie_name)


# The (name) and the argument we send (newbie_name) doesnt have to match

# The block of code in the function should make (name) and {name}

def fullname():
    print(f"Hey! Mr.{last_name}")
    print(f"Can I call you {first_name}")


first_name = input("What's your first name? ")

middle_name = input("What's your middle name? ")

last_name = input("What's your last name? ")

fullname()

# Lesson 21

# Return Statements

# Used in python to send python values/objects back to the caller

# These values/objects are known as the function's "return" values

def multiply(n1, n2):
    result = n1 * n2
    return result

multiply(6, 8)

def multiply(n1, n2):
    result = n1 * n2
    return result


print(multiply(6, 8))


# or x = multiply(6, 8) then, print(x)

def newmultiply(n1, n2):
    return n1 * n2


print(newmultiply(2, 4))


# Lesson 22

# Keyword Arguments

# Arguments preceded by an identifier when we pass them to a function
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our functions receive

def Hello(first, middle, last):
    print(f"Hello, {first} {middle} {last}")


# Whereas in positional arguments they have a order, and they follow it
# Just lke the name (They don't have identifiers)
print(Hello(first="Blue", middle="Pega", last="Cookie"))

# Lesson 23

# Nested Function Cells

# Function cells inside other function cells
# Innermost function cells are reolved first
# Returned value is used as an argument for the next outer function

print(round(abs(float(input("Enter a whole positive number: ")))))

# Lesson 24

# Variable Scope

# The region that a variable is recognised
# A variable is only available from inside the region is created
# A globally or locally scoped variable can be created

name = "Blue"  # global scope - available inside and outside function


def display_name():
    name = "Blue"  # local scope - available only inside the function


display_name()
print(name)


# Lesson 25

# *args

# Parameter that'll pack all arguments into a tuple
# Useful so that a function can can accept a varying amount of arguments

def add(n1, n2):
    sum = n1 + n2
    return sum


print(add(6, 11))


def new_add(*numbers):
    sum = 0
    # As it's a tuple the order is unchangable
    # So we'll cast it to a list
    numbers = list(numbers)
    numbers[3] = 0
    for i in numbers:
        sum += i
    return sum


print(new_add(39, 89, 9, 9384, 234))


# Lesson 26

# **kwargs

# parameters that'll pack all arguments into a dictionary
# Useful so that a function can accept a varying amount of keyword arguments

def hello(**names):
    print("Hello, " + names['first'] + " " + names['last'])


hello(last="Cookie", first="Blue")


def new_hello(**newnames):
    print("Hello", end=" ")
    for key, value in newnames.items():
        print(value, end=" ")


new_hello(first="Blue",  middle="_Pega", last="Cookie")

# Lesson 27

# str.format()

# Optional method which gives users more control when displaying output

animal = "cow"

item = "moon"

print("The {} jumped over the {}".format(animal, item))
# Order is important (Positional arguments) you can used indexing {0} in curly brackets


text = "The {} jumped over the {}! "
print(text.format(animal, item))

name = "Blue"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 23

print("The number is {:.3f}".format(number))
print("The number is {:,}".format(number))

print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))

# Lesson 29

# Random Numbers

import random

x = random.randint(1,109)
# The above code generates a number between 1 and 109

y = random.random()
# The above code generates a number between 0 and 1

print(x, y)

rpsmodule = ["rock", "paper", "scissors"]
computer_choice = random.choice(rpsmodule)

print(computer_choice)

# We could create a rock paper scissors game (1 player)!

a_suit_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

random.shuffle(a_suit_of_cards)

print(a_suit_of_cards)

# Lesson 29

# Exception Handling

# Exceptions are certain events that is seen while running a program and occur due to the faults in the code

numerator = int(input("Enter a number to divide: "))
denominator = int(input("Enter a number to divide by: "))
result = numerator / denominator
print(result)

# Well if the user enters '0' you'll receive a 'ZeroDivisionError' Which interrupts the programme

# This lesson will help you on how to handle these errors.

try:
    # A common solution to handling these errors are using the 'try' function
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except Exception:
    # This function allows use to provide a solution to the user for creating an error rather than showing# the error
    # itself!
    print("Something went wrong :(")
    # By simply enclosing all errors in this statement we can provide specific solutions to specific errors

# Although it's not a good practise to just give the same solution to all problems
# It's beneficial to return specific solutions to respective problems

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can divide numbers by 0 Dummy!")
except ValueError as e:
    print(e)
    print("Please enter only numbers!")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("Hope this helped! ")


# Lesson 30

# File Detection

import os

path = "F:\\Python notepad\\Folder Detector"

if os.path.exists(path):
    print("That location is true")
    if os.path.isfile(path):
        print("It's a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That locations does not exist")

# The above code must be replicated via a text file on your computer


# Lesson 31

# Reading a File

File_path = "F:\\Python notepad\\An Example Notepad.txt"
with open(File_path) as file:
    print(file.read())

print(file.closed)

# Generally if you open a file yu would have to close it.
# But as we've used the 'with' function it closes automatically!

# Although the above code is fine, it doesn't handle exceptions
# So just like weve learn in the previous lessons let's use our knowledge to handle these errors

try
    File_path = "F:\\Python notepad\\An Example Notepad.txt"
    with open(File_path) as file:
        print(file.read())
except FileNotFoundError:
    print("The file wasn't found please try again!")

# Lesson 32

# Writing a file

File_path = "F:\\Python notepad\\An Example Notepad.txt"

text = "Have a nice day\n See ya"

with open(File_path, 'a') as file:
    file.write(text)

# r = read - reading the contents of a file
# w = write - writing (overwriting) a file, if you write an existing file the previous contents will we be deleted
# a = append - it adds contents to a file, it doesn't delet previous contents


# Lesson 33

# Copying a file

import shutil

# copyfile() =  copies contents of a file
# copy()     =  copyfile() + permission modes + destination could be a directory
# copy2()    =  copy () + copies metadata (file's creation and modification times

shutil.copyfile("F:\\Python notepad\\An Example Notepad.txt", 'copy.txt') # source (src) and destination (dst)

# The Destination could also be anywhere on you personal computer like in a different drive folder.

# if you want to use the other two function just change shutil.copyfile() to shutil.copy() or shutil.copy2()


# Lesson 34

# Moving a file

import os

source = "F:\\Python notepad\\An Example Notepad.txt"

destination = "F:\\Python notepad\\File Destination"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + "Was moved!")
except FileNotFoundError:
    print(source + " was not found :( ")

# Lesson 35

# Deleting Files

import os

path = "empty directory"
try:
    # os.remove(path) # I made it a comment as it only works for files not empty folders
    os.rmdir(path) # This deletes an empty directory or folder
except FileNotFoundError:
    print("The file you want to delete does not exist")
    print("Yu must've misspelled the path way. Please Try Again!")
except PermissionError:
    print("You do not have the power (permission) to delete folders (directories)")
else:
    print(path + " Was deleted")

# Now lets attempt to delete a folder with files

new_path = "folder"

try:
    # os.rmdir(new_path) # This won't work for folder with files
    # for deleting folder with file you have to import shutil module
    import shutil
    shutil.rmtree(new_path)
    # It's really dangerous to use the above code as it will delete everything in that directory
    # Use it carefully, deleted file cannot be regained unless backed up :)
except FileNotFoundError:
    print("The file you want to delete does not exist")
    print("Yu must've misspelled the path way. Please Try Again!")
except PermissionError:
    print("You do not have the power (permission) to delete folders (directories)")
except OSError:
    print("You cannot delete a folder with a file with that function")
else:
    print(new_path + " Was deleted")


# Lesson 36

# Modules In Python

# What is a module?

# A module is a file containing python codes. May contain functions, classes, etc.
# Used in modular programming, which is, to separate a programme into parts

# Now let's say i have a function hello() in another file i.e workspace
# Before accessing it at the top please mention import (filenane)/(module) i.e in our case import workspace
# To access it all i have to do is (filename).(function) == workspace.hello()

# To shorten things upi could type    import workspace as ws
# Then ws.hello()
# anything in you prefer

# We can also shorten it even further by doing
# from workspace import hello() (You can add other functions via ,

# You could also do from workspace import *
# the above code imports every function
# Although i wouldn't recommend it as slows your computer if it has alot of modules (large programme)
# And you may run into naming conflicts and errors

# If you're working on a small programme then no worries

# If you want a comprehensive list of modules that python already has
# Enter the code
# help("Modules")

# You could also go to pythons official website where they have mentioned all modules
# docs.python.org/3/py-modindex.html
# Just copy that and paste it in a search browser


# Lesson 37

# For context, I have finished for 4 insisted side quests.
# Although now i have a mandatory one, I'll Be naming it Project 01

# Lesson 38

# It was also a project Project X02

# Lesson 39

# Python Object Oriented Programming

# Aka POOP

# An object is an instance of a class

class Trial:
    pass

# If it's a big programme it's reccomended to open a new module and then create your class

class Car:

    wheels = 4 # Class Variables

    def __init__(self, make, model, year, colour):
        self.make = make     # Instance Variables
        self.model = model   # Instance Variables
        self.year = year     # Instance Variables
        self.colour = colour # Instance Variables

    def drive(self):
        print(f"This {self.model} is driving")

    def stop(self):
        print(f"This {self.model} is stopped")


car_1 = Car("Checy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)
print(car_1.wheels)

car_1.drive()
car_1.stop()

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.colour)
print(car_2.wheels)

car_2.drive()
car_2.stop()

# That was just the basics by the way

# Lesson 40

# Class Variables

# ~ Instance Variable ~
# Variables declared within the constructor (__init__) are know as instance variables
# And each object can have a variable assigned to them

# ~ Class Variable ~
# Setting a default value for a variable used throughout the class (constant)
# Its declared within a class variable but outside the constructor (__init__).

# If you look at the previous lesson i've added comments for alignment purposes.

# Lesson 41

# Inheritance

# Classes usually inherit attributes and methods from another class

# They usually form parent child relationship

class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("The animal is sleeping")


class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")


class Fish(Animal):

    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive) # using print function because it's a boolean value
fish.eat()  # Not using print function cause it's already a function dummy
hawk.sleep()# The same clause from above

# 2 Benefits of using inheritance

# 1. Even though we don't have anything inside the class itself due to having another class inside it's brackets we
# can access them all without having to write anything similar within them

# 2. Once the code has been written we don't have to write the same code again and again for multiple children By
# doing this we don't have to change the term over and over again as if we change it in the parent variable. It'll be
# changed for every other instance

# Each child class can have their own personal specific attributes too! No restrictions

rabbit.run()
fish.swim()
hawk.fly()

# The above is an example for the previous statement


# Lesson 42

# Multi Level Inheritance

# When a derived class or child class inherits from another derived class or child class

class Organism:
    alive = True


class Animal(Organism):

    def eat(self):
        print("This animal is eating")


class Dog(Animal):

    def bark(self):
        print("This dog is barking")

# This is multiple inheritance

# Derived Class (aka Child Class) which is Animal inherits from Parent Class Organism
# Now the class dog which is also a derived class inherits from another derived class

# A hierarchy to make more sense

dog = Dog()
# This step is to make thing easier when writing larger code >_<.


print(dog.alive)
# Although print(Dog().alive) also works

dog.eat()
dog.bark()

# That was proof this works as it receives the alive and eat from respective classes and it does not have the variable
# withing its personal class

# Think of it like a family tree :)


# Lesson 43

# Multiple Inheritance

# It's the concept where a child class is derived from two different parent classes

class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal hunts")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

# You can see that the fish has inherited both prey feature and predator feature from two different parent class

