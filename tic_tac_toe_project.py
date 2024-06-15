from random import randrange

board=[[1,2,3],[4,'X',6],[7,8,9]]

def display_board(board):
    print("+-------"*3+"+")
    for row in range(3):
        print("|       "*3+"|")
        for col in range(3):
            print("|   "+str(board[row][col])+"   ",end="")
        print("|")
        print("|       "*3+"|")
        print("+-------"*3+"+")

def enter_move(board):
    flag = False                                 # condition to break loop 
    while not flag:
        move = input("Enter your move: ")                     
        flag = len(move)==1 and move>'0' and move<='9'             # check if the input is a valid number
        if not flag:
            print("Invalid Input, try again! ")                    # if not, take input again!
            continue
        move = int(move)-1                                           
        row = move//3
        col = move%3
        status = board[row][col] 
        flag = status not in ['O','X']                              # checking the status of the cell selected
        if not flag: 
            print("This Field was already selected, choose again! ")          # if the cell was already selected before then take the input again!
            continue
    board[row][col] = 'O'                                         # else set 'O' in the selected cell


def free_fields_list(board):
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X','O']:        # if cell is free
                free.append((row,col))                  # append the tuple to the list
    return free


def victory_for(board,sign):
    if sign == 'X':                 # if sign is "X" its for computer
        victor = 'me'
    elif sign == 'O':               # if sign is "O" its for user
        victor = 'you'
    else:
        victor = None
    diag1 = diag2 = True           # for diagonals 
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:         # rows
            return victor
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:         #columns
            return victor
        if board[i][i] != sign:                                  #diagonal1
            diag1 = False
        if board[i][2-i] != sign:                                #diagonal2
            diag2 = False
    if diag1 or diag2:
        return victor
    return None

def draw_move(board):
    free = free_fields_list(board)           # get the list of tuples of free fields in (row, col) form
    count = len(free)                        # number of free fields
    if count>0:                      
        index = randrange(count)             # generating random number for the index
        row, col = free[index]               # assigning the row and col at that index to row and col variable
        board[row][col] = 'X'                # setting the field to 'X'
    

free = free_fields_list(board)
user_turn = True
while len(free):
    display_board(board)
    if user_turn:
        enter_move(board)
        victor = victory_for(board,'O')
    else:
        draw_move(board)
        victor = victory_for(board,'X')
    if victor != None:
        break
    user_turn = not user_turn
    free = free_fields_list(board)

display_board(board)
if victor == 'me':
    print("I Won! ")
elif victor == 'you':
    print("You Won! ")
else:
    print("It's a tie!!")

