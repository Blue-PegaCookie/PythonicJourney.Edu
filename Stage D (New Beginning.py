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


def Howdie(name):
    print(f"Hey Man, Your name is {name} right?")
    print("Well... Welcome!")


newbie_name = "Blue_PegaCookie"

Howdie(newbie_name)


# The (name) and the argument we send (newbie_name) doesnt have to match

# The block of code in the function should make (name) and {name}

def Full_Name(first_name, middle_name, last_name):
    print(f"Hey! Mr.{last_name}")
    print(f"Can I call you {first_name}")


firstname = input("What's your first name? eh? ")

middle_name = input("What's your middle name coward! ")

lastname = input("What's your last name! ")

Full_Name(firstname, middlename, lastname)

