from random import randint

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
    question = input("Ask a yes-no question: ")
    answer = outputs[randint(0, len(outputs)-1)]
    print(answer)
    again = input("Would you like to ask anoter question? [y/n]: ")
    if again.lower() != "y":
        break
