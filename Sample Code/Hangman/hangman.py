from random import randint

words = [
    "apple",
    "banana",
    "fire",
    "dog",
    "trophy",
    "pineapple",
    "movie"
]

while True:
    randomNumber = randint(0, len(words)-1)
    word = words[randomNumber]
    userCorrect = []
    userIncorrect = []
    incorrectCount = 0
    for dash in range(len(word)):
        print("_", end=" ")
        userCorrect.append("_")
    print()
    while incorrectCount < 5:
        userLetter = input("Type a letter\n")
        index = 0
        if userLetter in userCorrect or userLetter in userIncorrect:
            print("You already used that letter. Try again")
            for letter in userCorrect:
                print(letter, end=" ")
            print()
        elif len(userLetter) > 1:
            print("Only 1 letter is allowed.")
            for letter in userCorrect:
                print(letter, end=" ")
            print()
        else:
            for letter in word:
                if userLetter == letter:
                    userCorrect[index] = letter
                index += 1
            if not userLetter in word:
                print("The letter is not in the word.")
                userIncorrect += userLetter
                incorrectCount += 1
            for letter in userCorrect:
                print(letter, end=" ")
            print()
            if not "_" in userCorrect:
                break
    print("Game Over")
    if "_" in userCorrect:
        print("You lost")
        print("The word was", word)
    else:
        print("You won")
    again = input("Do you want to play again? [yes/no]\n")
    if again == "no":
        break