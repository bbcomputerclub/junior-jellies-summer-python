while True:
    row1 = ["_", "_", "_"]
    row2 = ["_", "_", "_"]
    row3 = ["_", "_", "_"]
    board = [row1, row2, row3]
    xTurn = True
    xSpots = []
    oSpots = []
    while True:
        if xTurn: 
            print("X's turn")
        else:
            print("O's turn")
        row = int(input("Pick a row: ")) - 1
        column = int(input("Pick a column: ")) - 1
        if board[row][column] != "_":
            print("That spot is already taken")
            for row in board:
                for spot in row:
                    print(spot, end=" ")
                print()
            print()
        else:
            if xTurn:
                board[row][column] = "X"
            else:
                board[row][column] = "O"
            xTurn = not xTurn
            for row in board:
                for spot in row:
                    print(spot, end=" ")
                print()
            print()
            sameLetter = 0
            # Goes through each row and checks to see if they are all the same for X
            for row in board:
                for spot in row:
                    if spot == "X":
                        sameLetter += 1
                if sameLetter == 3:
                    break
                sameLetter = 0
            if sameLetter == 3:
                print("Game over")
                print("X won")
                break
            # Goes through each row and checks to see if they are all the same for X
            for row in board:
                for spot in row:
                    if spot == "O":
                        sameLetter += 1
                if sameLetter == 3:
                    break
                sameLetter = 0
            if sameLetter == 3:
                print("Game over")
                print("O won")
                break
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
    again = input("Do you want to play again [yes/no]\n")
    if again == "no":
        break