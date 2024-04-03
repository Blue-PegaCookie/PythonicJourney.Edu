# Rock Papaer Scissors Game (Final Fixing

def introduction():
    print("Hey Everyone")
    print("This is Lesson 37 aka Project X01")
    print("The reason i have done this is because I will be creating a game")


def hello():
    print("Welcome To Rock Paper Scissors! ")


import random


def rps():
    choices = ["rock", "paper", "scissors"]

    computer_choice = random.choice(choices)

    player_choice = input("Rock, Paper, Scissors: ").lower()

    while True:
        while player_choice not in choices:
            print("You have to choose any one of the following! ")
            player_choice = input("Rock, Paper, Scissors: ").lower()
        if player_choice in choices:
            if player_choice == computer_choice:
                print(f"You chose {player_choice} and the computer chose {computer_choice}, So it's draw!")
            elif player_choice == "rock":
                if computer_choice == "paper":
                    print(f"You chose {player_choice}, the computer chose {computer_choice}, So you lost")
                elif computer_choice == "scissors":
                    print(f"You chose {player_choice}, the computer chose {computer_choice}, So you won")
                else:
                    print("There must've been something wrong!")
            elif player_choice == "paper":
                if computer_choice == "rock":
                    print(f"You chose {player_choice}, the computer chose {computer_choice}, So you won")
                elif computer_choice == "scissors":
                    print(f"You chose {player_choice}, the computer chose {computer_choice}, So you lost")
                else:
                    print("There must've been something wrong!")
            elif player_choice == "scissors":
                if computer_choice == "paper":
                    print(f"You chose {player_choice}, the computer chose {computer_choice}, So you won")
                elif computer_choice == "rock":
                    print(f"You chose {player_choice}, the computer chose {computer_choice}, So you lost")
                else:
                    print("There must've been something wrong!")
        else:
            print("There must've been something wrong!")

        break

    pg = input("Do you want to play again? ").lower()

    options = ["y", "yes", "n", "no"]

    while pg not in options:
        print("Choose yes or no. Please!")
        pg = input("Do you want to play again? ").lower()

        if pg == "n" or "no":
            print("Thank you for playing! ")
        elif pg == "y" or "yes":
            print("Good Luck")
            rps()
        else:
            print("Choosepape yes or no please")
        break

rps()
