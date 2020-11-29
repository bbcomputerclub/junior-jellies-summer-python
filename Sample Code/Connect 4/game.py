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

    player_turn = 1
    
    board = generate_board()
    
    num_players = int(input("How many players are going to play Connect 4: "))
    player_names = []
    for i in range(num_players):
        player_names.append(input("Type player " + str(i + 1) + "'s name: "))

    print()

    

    while True:
        print(player_names[player_turn - 1] + "'s turn")
        print()
        print_board(board)
        print()
        try:
            column = int(input("Which column do you want to place your piece? ")) - 1
            column_already_filled = board[0][column] != "_"
        except (ValueError, IndexError):
            print()
            print("Invalid input, please try again")
            print()
            continue
        if column_already_filled:
            print()
            print("The column is already filled. Please try another column")
            print()
            continue
            
        if board[len(board) - 1][column] == "_":
            board[len(board) - 1][column] = player_turn
        else:
            for row in range(len(board)):
                if board[row][column] != "_":
                    board[row - 1][column] = player_turn
                    break

        player_has_won = check_rows(board, player_turn) or check_columns(board, player_turn) or check_diagonals(board, player_turn)

        if player_has_won:
            print_board(board)
            print()
            print("Player", str(player_turn), "won!")
            break
        elif check_board_filled(board):
            print_board(board)
            print()
            print("Tie game!")
            break

        player_turn = player_turn % num_players + 1
        print()

play_game()