def generate_board():
    board = []
    row = []
    for _ in range(6):
        for _ in range(7):
            row.append("_")
        board.append(row)
        row = []
    return board

def print_board(board):
    for row in board:
        for spot in row:
            print(spot, end=" ")
        print()
    print()
    for column in range(len(board[0])):
        print(column + 1, end=" ")
    print()

def check_winner(board, player_one_turn):
    piece = ""
    if player_one_turn:
        piece = "X"
    else:
        piece = "O"
    return check_rows(board, piece) or check_columns(board, piece) or check_diagonals(board, piece)

def check_rows(board, piece):
    consecutive_piece_count = 0
    for row in board:
        consecutive_piece_count = 0
        for spot in row:
            if spot == piece:
                consecutive_piece_count += 1
            else:
                consecutive_piece_count = 0
            if consecutive_piece_count == 4:
                return True
    return False
        
def check_columns(board, piece):
    consecutive_piece_count = 0
    for column in range(len(board[0])):
        consecutive_piece_count = 0
        for row in range(len(board)):
            if board[row][column] == piece:
                consecutive_piece_count += 1
            else:
                consecutive_piece_count = 0
            if consecutive_piece_count == 4:
                return True
    return False

def check_diagonals(board, piece):
    consecutive_piece_count = 0
    row_index = 0
    column_index = 0
    for row in board:
        consecutive_piece_count = 0
        for spot in row:
            if spot == piece:
                consecutive_piece_count = 1
                temp_row = row_index
                temp_column = column_index
                while consecutive_piece_count != 0 and consecutive_piece_count != 4:
                    temp_row += 1
                    temp_column += 1
                    if temp_row < len(board) and temp_column < len(board[temp_row]):
                        if board[temp_row][temp_column] == piece:
                            consecutive_piece_count += 1
                        else:
                            consecutive_piece_count = 0
                    else:
                        break
                if consecutive_piece_count == 4:
                    return True
                consecutive_piece_count = 1
                temp_row = row_index
                temp_column = column_index
                while consecutive_piece_count != 0 and consecutive_piece_count != 4:
                    temp_row += 1
                    temp_column -= 1
                    if (temp_row >= 0 and temp_column >= 0) and (temp_row < len(board) and temp_column < len(board[temp_row])):
                        if board[temp_row][temp_column] == piece:
                            consecutive_piece_count += 1
                        else:
                            consecutive_piece_count = 0
                    else:
                        break
                if consecutive_piece_count == 4:
                    return True
            column_index += 1
        row_index += 1
        column_index = 0
    row_index = 0
    column_index = 0
    return False

def check_board_filled(board):
    for row in board:
        for spot in row:
            if spot == "_":
                return False
    return True

def play_game():

    player_one_turn = True
    
    board = generate_board()
    
    print()

    while True:
        if player_one_turn:
            print("Player 1's turn")
        else:
            print("Player 2's turn")
        print()
        print_board(board)
        print()
        column = int(input("Which column do you want to place your piece? ")) - 1

        column_already_filled = board[0][column] != "_"
        if column_already_filled:
            print()
            print("The column is already filled. Please try another column")
            print()
            continue
            
        if board[len(board) - 1][column] == "_":
            if player_one_turn:
                board[len(board) - 1][column] = "X"
            else:
                board[len(board) - 1][column] = "O"
        else:
            for row in range(len(board)):
                if board[row][column] != "_":
                    if player_one_turn:
                        board[row - 1][column] = "X"
                    else:
                        board[row - 1][column] = "O"
                    break
            
        if check_winner(board, player_one_turn):
            print_board(board)
            print()
            if player_one_turn:
                print("Player 1 won!")
            else:
                print("Player 2 won!")
            break
        elif check_board_filled(board):
            print_board(board)
            print()
            print("Tie game!")
            break

        player_one_turn = not player_one_turn
        print()

play_game()