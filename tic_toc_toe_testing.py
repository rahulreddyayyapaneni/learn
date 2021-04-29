from random import randrange

moves = [[1,2,3],[4,5,6],[7,8,9]]
O_fields = []
X_fields = []
free_fields = []
all_fields = []
O_Result = ""
X_Result = ""
X_moves = []
O_moves = []
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(4):
        print("+--------+-------+-------+")
        print("| \t | \t | \t |")
        print("|    "+str(board[i][0])+"   |   "+str(board[i][1])+"   |   "+str(board[i][2])+"   |")
        print("| \t | \t | \t |")
        if i == 2:
            print("+--------+-------+-------+")
            break


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    cur_stat = draw_move(board)
    # print(cur_stat)
    # print("O_Result:",O_Result)
    # print("X_Result:",X_Result)
    if (O_Result or X_Result) != True:
        
        e = int(input("Enter your move: "))
        a = -1
    
        # print(new)
        for i in board:
            b = -1
            a += 1
            for j in i:
                b += 1
                new=[]
                new.append(j)
                # print("new:",new)
                # print("a:",a,"b:",b)
                # print("moves[a][b]:",moves[a][b])
                
                if e in new and (a,b) not in O_fields:
                    # print("i",i)
                    # print("j",j)
                    # if new == 'O' or new == 'X':
                    #     print("Please choose a free move")
                    # else:
                    board[a][b] = 'O'
                    O_moves.append(e)
                    O_fields.append((a,b))
                    display_board(board)
                    # print("O_fields:",O_fields)
                    victory_for(board,"O")
                    return
                        
            # else:
            #     print("Please choose a free move")

        # cur_stat = display_board(board)
        # # print(cur_stat)
        # c = -1
        # for i in board:
        #     d = -1
        #     c += 1
        #     for j in i:
        #         d += 1
        #         new=[]
        #         new.append(j)
        #         # print(new)
        #         # print("c:",c,"d:",d)
        #         # print("board[c][d]:",board[c][d])
        #         if 'O' in new and (c,d) not in O_fields:  
                    
        #             O_fields.append((c,d))
                    
        #         elif 'X' in new and (c,d) not in X_fields:
                    
        #             X_fields.append((c,d))
    
        # print("O_fields:",O_fields)
        # # print("X_fields:",X_fields)
    
    else:
        # print("No Choice, User Returning back")
        return

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    # global free_fields = []
    a = -1
    for i in board:
        b = -1
        a += 1
        for j in i:
            b += 1
            new=[]
            new.append(j)
            # print(new)
            # print("a:",a,"b:",b)
            # print("inputt[a][b]:",board[a][b])
            if 'O' in new or 'X' in new:
                
                print("Not an Interger, May be 'O' or 'x'")
                
            else:
                free_fields.append((a,b))
    
    print(free_fields)
    
# O_fields = []
# X_fields = []
# O_Result = ""
# X_Result = ""

def victory_for(board,sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    global O_fields
    global X_fields
    global O_Result
    global X_Result
    
    a = -1
    
    alpha = [(0,0),(0,1),(0,2)]
    beta = [(1,0),(1,1),(1,2)]
    gaama = [(2,0),(2,1),(2,2)]
    fstcol = [(0,0),(1,0),(2,0)]
    sndcol = [(0,1),(1,1),(2,1)]
    trdcol = [(0,2),(1,2),(2,2)]
    fstdiag = [(0,0),(1,1),(2,2)]
    snddiag = [(2,0),(1,1),(0,2)]
    matching = [alpha,beta,gaama,fstcol,sndcol,trdcol,fstdiag,snddiag]
    all_fields = X_fields + O_fields
    # for i in board:
    #     b = -1
    #     a += 1
    #     for j in i:
    #         b += 1
    #         new=[]
    #         new.append(j)
    #         # print(new)
    #         # print("a:",a,"b:",b)
    #         # print("inputt[a][b]:",board[a][b])
    #         if 'O' in new:  
                
    #             O_fields.append((a,b))
                
    #         elif 'X' in new:
                
    #             X_fields.append((a,b))
    
    # print("O_fields:",O_fields)
    # print("X_fields:",X_fields)
    
    # for j in matching:
        
        # if ( len(O_fields) or len(X_fields) ) == len(j):
            
        #     if j == O_fields and sign == "O":
                
        #         print("You Won!")
        #         return True
            
        #     elif j == X_fields and sign == "X":
                
        #         print("Machine Won!")
        #         return False
    # print("Now X_fields has count of",len(X_fields))
    # print("Now O_fields has count of",len(O_fields))
        
    if  len(O_fields) or len(X_fields)  >= 3:
        # print("Start Validating")    
        for i in matching:
            # print("i:",i)
            O = 0
            X = 0
            for j in i:
                # print("j:",j)
                if j in O_fields and sign == "O":
                    O += 1
                    # print("got into validation loop for O")
                    # print("j: ",j)
                    # print("O:",O)
                        
                    if O != 3:
                        continue
                        # enter_move(board)
                        # print (False)
            
                    elif O >= 3:
                        # print("i: ",i,"O_fields:",O_fields)
                        O_Result = True
                        print("******You Won, Machine Lost******")
                        return
                        
                elif j in X_fields and sign == "X":
                    X += 1
                    # print("got into validation loop for X:",X)
                    # print("j: ",j)
                    # print("X:",X)
                        
                    if X != 3:
                        continue
                        # enter_move(board)
                        # print (False)
            
                    elif X == 3:
                        # print("j: ",j,"X_fields:",X_fields)
                        X_Result = True
                        print(":::::::Machine Won, better luck next time:::::::")
                        return
                        
    elif (len(O_fields) == len(X_fields)) and (all_fields.sort() == free_fields):
        print("No moves left")
        # if all_fields.sort() == free_fields:
        O_Result = False
        # X_Result = False
        print("}-}-}-}-}-}-}-}-} It's a Draw, Go Straight and take left {-{-{-{-{-{-{-{-{")
                
    else:
        # print("Returning back from validation")
        return
    
    if O_Result == True and sign == "O":
        
        print("******You Won, Machine Lost******")
        
    
    elif X_Result == True and sign == "X":
        
        print(":::::::Machine Won, better luck next time:::::::")
        
    
    
    


def draw_move(board):
    # The function draws the computer's move and updates the board.
    # cur_stat = display_board(board)
    # print(cur_stat)
    if (O_Result or X_Result) != None:
        e = randrange(1,10)
        # print("e:",e)
        # print("X_moves:",X_moves)
        # print("O_moves:",O_moves)
        
        if e in X_moves or e in O_moves:
            call_again = draw_move(board)
            # print(call_again)
        
        new=[]
        a = -1
        for i in board:
            b = -1
            a += 1
            for j in i:
                b += 1
                
                new.append(j)
                # print(new)
                # print("a:",a,"b:",b)
                # print("moves[a][b]:",board[a][b])
                
                if e in new and (a,b) not in X_fields:
                    board[a][b] = 'X'
                    X_moves.append(e)
                    display_board(board)
                    X_fields.append((a,b))
                    # print("X_fields:",X_fields)
                    victory_for(board,"X")
                    return 
    
        # c = -1
        # for i in board:
        #     d = -1
        #     c += 1
        #     for j in i:
        #         d += 1
        #         new=[]
        #         new.append(j)
        #         # print(new)
        #         # print("c:",c,"d:",d)
        #         # print("board[c][d]:",board[c][d])
        #         if 'O' in new and (c,d) not in O_fields:  
                    
        #             O_fields.append((c,d))
        #             # print("O_fields:",O_fields)
                    
        #         elif 'X' in new and (c,d) not in X_fields:
                        
        #             X_fields.append((c,d))
        #             print("X_fields:",X_fields)
    
    
                    
                # elif e in X_moves:
                #     call_again = draw_move(board)
                #     print(call_again)
            # break
    else:
        # print("Machine Returning back")
        return

# result1 = victory_for(moves,"O")
# result2 = victory_for(moves,"X")
# Func1 = diplay_board(moves)
# Func2 = enter_move(moves)
# Func3 = make_list_of_free_fields(moves)
# Func5 = draw_move(moves)

while (O_Result or X_Result) != True:
    
    # if (len(O_fields) or len(X_fields)) <= 3:
        
    if len(free_fields) == 0:
        start  = make_list_of_free_fields(moves)
        # draw_move(moves)
        
    elif len(free_fields) == 9:
        enter_move(moves)
        # print("X_fields:",X_fields)
        # print("O_fields:",O_fields)    

    # elif len(free_fields) == 9:
    #     enter_move(moves)
    #     # print("X_fields:",X_fields)
    #     # print("O_fields:",O_fields)
    
    if (len(O_fields) or len(X_fields)) >= 3:
        
        # print("Now X_fields has count of",len(X_fields))
        # print("Now O_fields has count of",len(O_fields))
        # victory_for(moves,"X")
        # victory_for(moves,"O")
        
        if len(X_fields) >= 3:
            # print("goin to victory_for X")
            victory_for(moves,"X")
            continue
            
        elif len(O_fields) >= 3:
            # print("goin to victory_for O")
            victory_for(moves,"O")
            break
        
    
    # elif (len(O_fields) or len(X_fields)) > 1:
        
    #     enter_move(moves)




