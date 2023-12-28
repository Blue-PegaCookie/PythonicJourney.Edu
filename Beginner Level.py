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

