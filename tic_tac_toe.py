#TIC TAC TOE without using function
turn='X'
moves=0
board=[[1,2,3],[4,5,6],[7,8,9]]
print("Player one = X\nPlayer 2 = O")
while moves<=9:
    #Displaying Board
    print("       |         |        ")
    print("  ",board[0][0],"  |  ",board[0][1],"    | ",board[0][2],"   ")
    print("_______________________")
    print("       |         |        ")
    print("  ",board[1][0],"  |  ",board[1][1],"    | ",board[1][2],"   ")
    print("_______________________")
    print("       |         |        ")
    print("  ",board[2][0],"  |  ",board[2][1],"    | ",board[2][2],"   ")
    print("\n\n")
    #Check game draw
    if moves == 9:
        print("Game draw")
        break
    #Player turn message (Whose turn now)
    if turn =='X':
        print("Player1 turn")
        choice=int(input("Enter choice number "))
    else:
        print("Player 2 turn")
        choice = int(input("Enter choice number "))
    #Check invalid entered number
    if choice<1 or choice> 9:
        print("You entered wrong choice ")
        continue
    #Assigning index to board , base on the entered value
    row=(choice-1)//3 # Row
    col=(choice-1)%3  # Column
    #Checking the position is free or already taken
    if board[row][col]=='X' or board[row][col]=='O':
        print("Position already taken ")
        continue
    #printing users symbol on the entered value of board
    if board[row][col] != 'X' and board[row][col] != 'O':
        board[row][col]=turn
    print("\n\n")
    print("       |         |        ")
    print("  ",board[0][0],"  |  ",board[0][1],"    | ",board[0][2],"   ")
    print("_______________________")
    print("       |         |        ")
    print("  ",board[1][0],"  |  ",board[1][1],"    | ",board[1][2],"   ")
    print("_______________________")
    print("       |         |        ")
    print("  ",board[2][0],"  |  ",board[2][1],"    | ",board[2][2],"   ")
    print("\n\n")
    #........Check for winner.........:
    for j in range(3):
        #row
        if board[j][0]==board[j][1]==board[j][2]:
            print(f"player {turn} wins the game : ")
            exit()
        #Column
        if board[0][j] == board[1][j] == board[2][j]:
            print(f"Player {turn} wins the game ... ")
            exit()
    #for diognal one
    if board[0][0]==board[1][1]==board[2][2]:
        print(f"player {turn} wins the game ")
        exit()
    #For diognal two
    if board[0][2]==board[1][1]==board[2][0]:
        print(f"player {turn} wins the game : ")
        exit()
    #Changing turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
    moves+=1

