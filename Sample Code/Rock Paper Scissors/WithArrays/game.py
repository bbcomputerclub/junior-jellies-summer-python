from random import randint

randomNum = randint(0, 2)
computerHand = ""

hands = ["rock", "scissors", "paper"]

computerHand = hands[randomNum]

userHand = input("Rock, Paper, or Scissors\n").lower()

if userHand in hands:
    print("Computer:", computerHand)
    if userHand == computerHand:
        print("Tie")
    elif (userHand == "rock" and computerHand == "scissors") or (userHand == "paper" and computerHand == "rock") or (userHand == "scissors" and computerHand == "rock"):
        print("You won")
    else:
        print("Computer won")
else:
    print("Invalid input.")
