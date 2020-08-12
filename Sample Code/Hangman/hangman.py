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
    # Grabs a random word from the list to use for the game
    randomNumber = randint(0, len(words)-1)
    word = words[randomNumber]

    # the two lists tracks the correct and incorreect letters that the person typed. 
    userCorrect = []
    userIncorrect = []

    #This loops generates the dashed lines to start the game
    for dash in range(len(word)):
        print("_", end=" ")
        userCorrect.append("_")
    print()
    
    #This loop limiits the incorrect answers that the user can type down to five
    while len(userIncorrect) < 5:
        # ask the user to type a letter
        userLetter = input("Type a letter\n")
        
        
        #next two if statements are just validation if statements
        #checks to see if the user has already typed that letter
        if userLetter in userCorrect or userLetter in userIncorrect:
            print("You already used that letter. Try again")
            # just prints the list of letters with the correct and unguessed letters
            for letter in userCorrect:
                print(letter, end=" ")
            print()
        # If the user typed more than one letter
        elif len(userLetter) > 1:
            print("Only 1 letter is allowed.")
            # just prints the list of letters with the correct and unguessed letters
            for letter in userCorrect:
                print(letter, end=" ")
            print()
        # the user typed one letter that hasn't typed yet
        else:
            # the index variable is going to be used to track the index of the userCorrect array that the letter belongs
            index = 0
            for letter in word:
                if userLetter == letter:
                    userCorrect[index] = letter
                index += 1
            # The letter is not in the word
            if not userLetter in word:
                print("The letter is not in the word.")
                userIncorrect += userLetter
            # This just reprints the list of letters with the correct and unguessed letters
            for letter in userCorrect:
                print(letter, end=" ")
            print()
            # this checks to see if the user has guessed all of the letters correctly
            if not "_" in userCorrect:
                break
    print("Game Over")
    # checks to see if the user hasn't guessed all of the letters
    if "_" in userCorrect:
        print("You lost")
        print("The word was", word)
    else:
        print("You won")
    # asks if the user wants to play again
    again = input("Do you want to play again? [yes/no]\n")
    if again == "no":
        break