# This code is not the most optimal solution, though it is designed to make it easy for beginener programmers to grasp
# exactly what's happening with the code
# Difficulty: Very Hard

while True:
    # Generates the rows
    row1 = ["_", "_", "_"]
    row2 = ["_", "_", "_"]
    row3 = ["_", "_", "_"]
    # Generates the board
    board = [row1, row2, row3]
    # This will track whether it is X's turn (True) or O's turn (False)
    xTurn = True
    # This will track all of the indexes that the X's are located on the board (0-8)
    xSpots = []
    # This will track all of the indexes that the O's are located on the board
    oSpots = []
    #plays game
    while True:
        # Just prints who's turn it is
        # Same as `if xTurn == True:`
        if xTurn: 
            print("X's turn")
        else:
            print("O's turn")
        
        # Asks the user to pick a row and a column to place their X or O
        row = int(input("Pick a row: ")) - 1
        column = int(input("Pick a column: ")) - 1

        # Validation: checks to see if the spot is already taken
        if board[row][column] != "_":
            print("That spot is already taken")
            for row in board:
                for spot in row:
                    print(spot, end=" ")
                print()
            print()
        else:
            # The spot is available
            if xTurn:
                board[row][column] = "X"
            else:
                board[row][column] = "O"
            
            # if xTurn is True, xTurn is now False and vice versa.
            xTurn = not xTurn

            # Prints the board
            for row in board:
                for spot in row:
                    print(spot, end=" ")
                print()
            print()

            # Goes through each row and checks to see if all of the letters on the row are X
            sameLetter = 0
            for row in board:
                for spot in row:
                    if spot == "X":
                        sameLetter += 1
                # There are three X's on the row
                if sameLetter == 3:
                    break
                sameLetter = 0
            if sameLetter == 3:
                print("Game over")
                print("X won")
                break

            # Goes through each row and checks to see if all of the letters on the row are X
            for row in board:
                for spot in row:
                    if spot == "O":
                        sameLetter += 1
                # There are three O's on the row
                if sameLetter == 3:
                    break
                sameLetter = 0
            if sameLetter == 3:
                print("Game over")
                print("O won")
                break
            
            # Goes through each column and checks to see if all of the letters on the column are X
            for column in range(3):
                for row in board:  
                    if row[column] == "X":
                        sameLetter += 1
                if sameLetter == 3:
                    break
                sameLetter = 0
            if sameLetter == 3:
                print("Game over")
                print("X won")
                break

            ## Goes through each column and checks to see if all of the letters on the column are O
            for column in range(3):
                for row in board:  
                    if row[column] == "O":
                        sameLetter += 1
                if sameLetter == 3:
                    break
                sameLetter = 0
            if sameLetter == 3:
                print("Game over")
                print("O won")
                break

            # Checks for diagonals
            if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
                print("Game over")
                print("X won")
                break
            if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
                print("Game over")
                print("O won")
                break
            if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
                print("Game over")
                print("X won")
                break
            if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
                print("Game over")
                print("O won")
                break

    # Asks if they want to play again
    again = input("Do you want to play again [yes/no]\n")
    if again == "no":
        break