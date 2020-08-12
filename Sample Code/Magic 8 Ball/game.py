from random import randint

# List of possible outputs for the 8 ball
outputs = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it"
]
while True:
    # Asks the user to enter a yes-no question
    question = input("Ask a yes-no question: ")
    # Takes a random output from the list of outputs
    answer = outputs[randint(0, len(outputs)-1)]#
    # Prints the output of the magic 8 ball
    print(answer)
    # asks if the user wants to play again
    again = input("Would you like to ask anoter question? [y/n]: ")
    # If the user typed anything but yes, don't play again
    if again.lower() != "y":
        break
