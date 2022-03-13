#-----------Global variables:

# Game board

board =["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

#If game still going
game_still_going = True

#Who won? Or tie?
current_player = "X"


def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

        
def play_game():
    #Display initial board
    display_board()

    while game_still_going: #This is a loop
        
        #Handle a single turn of an arbitrary player
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie")


def handle_turn(player):
    print( player + "'s turn")
    position =(input("Choose a position from 1-9: "))

    valid = False #Boolean 1 or 0 (True or False)   #Loop that runs in a boolean
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:    #First Checks if the input is valid between the range.
            position =(input("Choose a position from 1-9: "))

        position = int(position)-1 #Second it changes to the board position

        if board[position] == "-": #Third it checks if the board position available
            valid = True           #If it is available then it turns the boolean to True and it breaks the loop!
        else:
            print("Not valid, go again!")
    
    board[position] = player
                   
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #Set up global variables
    global winner
    #check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
        return
    return
    
def check_rows():
    global game_still_going
    #Check if any of the rows have all the same value and is not empty
    row_1 = board[0] == board[1]==board[2] !='-'
    row_2 = board[3] == board[4]==board[5] !='-'
    row_3 = board[6] == board[7]==board[8] !='-'
    #If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
        #return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
     

def check_columns():
    global game_still_going
    #Check if any of the columns have all the same value and is not empty
    column_1 = board[0] == board[3]==board[6] !='-'
    column_2 = board[1] == board[4]==board[7] !='-'
    column_3 = board[2] == board[5]==board[8] !='-'
    #If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
        #return the winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
     

def check_diagonals():
    global game_still_going
    #Check if any of the diagonals have all the same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] !='-'
    diagonal_2 = board[6] == board[4] == board[2] !='-'
    #If any diagonals does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
        #return the winner X or O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return 

 

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player =="X":    #With the double == you are CHECKING that the value is X
        #If current player was X then change it to O
        current_player ="O" #There is a common mistake here to put two =, in this case we leave just one so that the variable CHANGES.
    elif current_player=="O": 
    #if the current player was O, then it changes to X
        current_player ="X"
    return


    

play_game()
