import random

rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
choices = ["rock", "paper", "scissors"]

#rock = "rock"
#print(rules)
#print(rules["rock"])
#print(rules[rock])

def RPS():
    
    CPU = choices[random.randint(0,2)]
    user = input("What is your choice?: ").lower()

    if (rules[CPU] == user):
        print("Computer wins!")
    elif (CPU == user):
        print("It's a tie.")
    else:
        print("User wins!!")
        
    print(CPU, user)

playOn = "yes"

while playOn != "no":
    RPS()
    playOn = input("type 'no' if you want to stop playing: ")
