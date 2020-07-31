from random import randint

randomNum = randint(0, 2)
computerHand = ""

if randomNum == 1:
    computerHand = "rock"
elif randomNum == 2:
    computerHand = "paper"
else:
    computerHand = "scissors"

userHand = input("Rock, Paper, or Scissors\n").lower()

if userHand == "rock" or userHand == "paper" or userHand == "scissors":
    print("Computer:", computerHand)
    if userHand == computerHand:
        print("Tie")
    elif (userHand == "rock" and computerHand == "scissors") or (userHand == "paper" and computerHand == "rock") or (userHand == "scissors" and computerHand == "rock"):
        print("You won")
    else:
        print("Computer won")
else:
    print("Invalid input.")

