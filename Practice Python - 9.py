import random
"""
def guessNumber():
    number = random.randint(0, 9)
    guess = int(input("Guess the number (0-9): "))

    #if (guess == number):
    #    print("You guessed the number!")
    while (guess != number):
        guess = int(input("Try again: "))
        if (guess - 4 > number or guess + 4 < number):
            print("You are cold")
        else:
            print("You are hot")

    print("You guessed the number!")

playOn = "yes"

while playOn != "no":
    guessNumber()
    playOn = input("type 'no' if you want to keep playing: ")
        
"""

def guessNumber():
    number = random.randint(0, 9)
    guess = int(input("Guess the number (0-9): "))

    #if (guess == number):
    #    print("You guessed the number!")
    while (guess != number):
        if (guess - 5 > number or guess + 5 < number):
            print("You are cold")
        else:
            print("You are hot")
        guess = int(input("Try again: "))

    print("You guessed the number!")

playOn = "yes"

while playOn != "no":
    guessNumber()
    playOn = input("type 'no' if you want to keep playing: ")
