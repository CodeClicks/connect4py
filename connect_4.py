#First thing we will want to do is to create our board for Connect 4
def create_board():
    #create an empty board to start with
    board=[]
    for _ in range(6):
        row =[' ']*7
        board.append(row)
    return board

#Next we will want to create a function that will print our Connect 4 board
def print_board(board):
    #Print the connect 4 board
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print()
        print('-'*15)

#We will then want to create a function that will check whether the move the player is attempting to implement is a valid move or not
def is_valid_move(board, col):
    #Check if the move is valid
    if col < 0 or col >=7:
        return False
    return board[0][col] == ' '

#Now we will implement a function that lets our players make a move
def make_move(board, col, player):
    #Make a move on the board
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return True
    return False

#Lastly, we will want to make a function that checks for the winner, the most important and heavy lifting function yet
def check_winner(board, player):
    #Check if a player has won
    #check horizontally
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and \
            board[row][col+1] == player and \
            board[row][col+2] == player and \
            board[row][col+3] == player:
                return True
            
    #check Vertically
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and \
            board[row+1][col] == player and \
            board[row+2][col] == player and\
            board[row+3][col] == player:
                return True
    
    #Check Diagonally from top left to bottom right
    for row in range(3):
        for col in range(4):
            if board[row][col] == player and \
            board[row+1][col+1] == player and \
            board[row+2][col+2] == player and \
            board[row+3][col+3] == player:
                return True
    
    #Check diagonally from top right to bottom left
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == player and \
            board[row+1][col-1] == player and \
            board[row+2][col-2] == player and \
            board[row+3][col-3] == player:
                return True
    
    return False

#Lets now create the final and most important function, the play game function
def play_game():
    #Main game loop
    board = create_board()
    current_player ='X'

    while True:
        print_board(board)
        col = int(input(f"Player {current_player}, enter a column number (0-6): "))

        if is_valid_move(board, col):
            if make_move(board, col, current_player):
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif ' ' not in board[0]:
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Column is full. Try again.")
        else:
            print("Invalid move. Try again.")

play_game()


