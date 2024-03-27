# This is where I test codes then I add it to the main lessons!

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
