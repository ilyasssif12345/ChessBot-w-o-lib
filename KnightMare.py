import numpy as np
import time
# the board
board = np.array(
[['2r1' , '2n1'  ,'2b1'  , '2q '  , '2k '  , '2b2'  ,  '2n2' ,   '2r2'],[
  '2p1',  '2p2' ,  '2p3' ,  '2p4'  ,'2p5' , '2p6', '2p7', '2p8'  ],[
"   "  ,  "   "   ,    "   "  ,    "   "   ,      "   "    ,  "   "   ,    "   "   ,   "   " ],[
"   "  ,   "   "   ,    "   " ,     "   "    ,     "   " ,     "   "    ,   "   "  ,   "   "  ],[
"   "   , "   "   ,   "   "   ,  "   "   ,      "   "  ,   "   "  ,     "   "      ,"   "  ],[
"   "   , "   "  ,     "   "  ,    "   "   ,      "   "  ,  "   "  ,       "   " ,   "   "],[
"1p1","1p2" ,'1p3' ,'1p4' , '1p5' , '1p6','1p7','1p8']  ,[
'1r1' ,  '1n1' , '1b1'   , '1q '  ,  '1k ' , '1b2'  , '1n2' ,'1r2']])
# coordination :
C = {"a" : 0 , "b" : 1 , "c" : 2 , "d" : 3 , "e" : 4 , "f" : 5 , "g" : 6 , "h":7}
# notation translator:
def tran(notation , inv):
    if inv == "off":
       x , y = C[notation[0]] , int(notation[1]) - 1
       return x , y
    else:
        for i in C:
            if C[i] == notation:
                return (i + str(inv+1))

        
#book moves:
kings_indian = {0:"g7g6" , 1:"f8g7:" , 2:"e7e6"}
# move possibility :
def N_moves(x , y,board9,opposite_turn):
       poss_moves = []
       for i in range(1,3):
         for n in range(1,3):
           for m in range(1,3):
             z , e = int((x + (2/i)*(-1)**n)) , (y + i*(-1)**m)
             try:
              if (board9[7-e, z] == " x "  or board9[7-e, z][0] == opposite_turn) and 7-e >= 0 and z >= 0:
               poss_move = tran(z , e)
               poss_moves.append(f"{tran(x,y)}{poss_move}")
             except:
              pass
       return poss_moves
   
def R_moves(x , y,board9,opposite_turn):
    poss_moves = []

    for i in range(2,4):
       e = y
       try:
         for j in range(1,8):
           if board9[ int(7 - (e + (-1)**i)) , x] == "   "  and int(7 - (e + (-1)**i)) >= 0 and x>=0:
            e = int(e + (-1)**i)
            poss_move = tran(x , e)
            f"{tran(x, y)}{poss_move}"
            poss_moves.append(f"{tran(x,y)}{poss_move}")
           elif board9[int(7 -  (e + (-1)**i)) , x][0] == opposite_turn and int(7 - (e + (-1)**i)) >= 0 and x>=0:
            e = int(e + (-1)**i)
            poss_move = tran(x , e)
            poss_moves.append(f"{tran(x,y)}{poss_move}")
            break
           else:
               break
       except:
          pass
    for i in range(2,4):
       e = x
       try:
        for j in range(1,8):
          if board9[7 -y ,int(e + 1*(-1)**i)] == "   "  and 7-y >= 0 and int(e + 1*(-1)**i) >=0:
            e = e + (-1)**i
            poss_move = tran(e , y)
            poss_moves.append(f"{tran(x,y)}{poss_move}")
          elif board9[7 - y ,int(e + 1*(-1)**i)][ 0] == opposite_turn and 7-y >= 0 and int(e + 1*(-1)**i) >=0:
            e = e + (-1)**i
            poss_move = tran(e , y)
            poss_moves.append(f"{tran(x,y)}{poss_move}")
            break
          else:
              break
       except:
          pass
    return poss_moves

def B_moves(x ,y ,board9,opposite_turn):
    poss_moves = []
    for p in range(1,3):
       for u in range(1,3):
        try:
          z , e = x , y
          for j in range(1,8):
            if board9[ int(7 -( e + (-1)**u)) , int(z +(-1)**p) ] == "   "  and int(7 -( e + (-1)**u)) >= 0 and int(z +(-1)**p) >= 0:
              z , e = z + (-1)**p , e + (-1)**u
              poss_move = tran(int(z) , int(e))
              poss_moves.append(f"{tran(x,y)}{poss_move}")
            elif board9[int(7-( e + (-1)**u )), z +(-1)**p][0] == opposite_turn and int(7 -( e + (-1)**u)) >= 0 and int(z +(-1)**p) >= 0:
               z , e = z + (-1)**p , e + (-1)**u
               poss_move = tran(int(z) , int(e))
               poss_moves.append(f"{tran(x,y)}{poss_move}")
               break
        except:
          pass

    return poss_moves


def Q_moves(x , y,board,opposite_turn):
    poss_moves = R_moves(x ,y,board,opposite_turn)
    for i in B_moves(x , y,board,opposite_turn):
       poss_moves.append(i)
    return poss_moves

def P_moves(x,y,board9,opposite_turn):
    if opposite_turn == "2":
     poss_moves = []
     if y == 1:
        if board9[6-y, x] == "   "  and 6-y >= 0 and x >= 0:
           if board9[5 - y , x] == "   "  and 5-y >= 0 and x >= 0:
              for i in range(1,3):
                 poss_moves.append(f"{tran(x,y)}{tran(x , y+i)}")
           else:
              poss_moves.append(f"{tran(x,y)}{tran(x , y +1)}")
     elif y != 1 :
        if board9[6 - y , x] == " x "  and 6-y >= 0 and x >= 0:
            poss_moves.append(f"{tran(x,y)}{tran(x , y+1)}")
     for i in range(1 ,3):
      try:
       if board9[ 6 -y , x +(-1)**i][0] == opposite_turn and 6-y >= 0 and x +(-1)**i >= 0:
          poss_moves.append(f"{tran(x,y)}{tran(x +(-1)**i , y +1)}")
      except:
          pass
     return poss_moves
    if opposite_turn == "1":
        poss_moves = []
        if y == 6:
            if board9[8-y, x] =="   "  and 8-y >= 0 and x >= 0:
                if board9[9-y, x] == "   "  and 9-y >= 0 and x >= 0:
                    for i in range(1, 3):
                        poss_moves.append(f"{tran(x, y)}{tran(x, y - i)}")
                else:
                    poss_moves.append(f"{tran(x, y)}{tran(x, y - 1)}")
        elif y != 6:
            if board9[8-y, x] == "   "  and 8-y >= 0 and x >= 0:
                poss_moves.append(f"{tran(x, y)}{tran(x, y - 1)}")
        for i in range(1, 3):
            try:
                if board9[8-y, x + (-1) ** i][0] == opposite_turn and 8-y >= 0 and x + (-1) ** i >= 0:
                    poss_moves.append(f"{tran(x, y)}{tran(x + (-1) ** i, y - 1)}")
            except:
                pass
        return poss_moves
def K_moves(x , y , board9,opposite_turn):
    poss_moves = []
    move_list = [(x , y+1) , (x , y-1) , (x + 1, y) , (x -1 , y) , (x+1 , y+1) , (x + 1 , y -1) , (x-1 , y+1) , (x-1 , y-1)]
    for z , e in move_list:
        try :
           if board9[7 -e , z] == "   "  or board9[7 -e , z][0] == opposite_turn and 7 -e >= 0 and z >= 0:
              poss_moves.append(f"{tran(x , y)}{tran(z , e)}")
        except:
            pass
    return poss_moves


# Choosing the best move:
def all_moves(board ,opposite_turn):
    all_poss = []
    # finding all the possible moves:
    if opposite_turn == "2":
      for z in range(0,8):
        for e in range(0,8):
          if board[7-e , z][0:2] == "1k":
             for o in K_moves( z ,e,board ,opposite_turn):
                 all_poss.append(o)
          if board[7-e , z][0:2] == "1q":
              for o in Q_moves(z, e,board,opposite_turn):
                  all_poss.append(o)
          if board[7-e , z][0:2] == "1b":
              for o in B_moves(z, e,board,opposite_turn):
                  all_poss.append(o)
          if  board[7-e , z][0:2] == "1r":
              for o in R_moves(z, e,board,opposite_turn):
                  all_poss.append(o)
          if board[7-e , z][0:2] == "1p":
              list = P_moves(z, e,board,opposite_turn)
              for o in list:
                  all_poss.append(o)
          if board[7-e , z][0:2] == "1n":
              for o in N_moves(z, e,board,opposite_turn):
                  all_poss.append(o)
    elif opposite_turn == "1":
         for z in range(0, 8):
             for e in range(0, 8):
                 if board[7 - e, z][0:2] == "2k":
                     for o in K_moves(z, e, board, opposite_turn):
                         all_poss.append(o)
                 if board[7 - e, z][0:2] == "2q":
                     for o in Q_moves(z, e, board, opposite_turn):
                         all_poss.append(o)
                 if board[7 - e, z][0:2] == "2b":
                     for o in B_moves(z, e, board, opposite_turn):
                         all_poss.append(o)
                 if board[7 - e, z][0:2] == "2r":
                     for o in R_moves(z, e, board, opposite_turn):
                         all_poss.append(o)
                 if board[7 - e, z][0:2] == "2p":
                     list = P_moves(z, e, board, opposite_turn)
                     for o in list:
                         all_poss.append(o)
                 if board[7 - e, z][0:2] == "2n":
                     for o in N_moves(z, e, board, opposite_turn):
                         all_poss.append(o)
    return all_poss

# this algorithm is commonly used in bot making ,I made some changes to make it compatible with the program
def minimax(board ,turn, alpha , beta,depth ,return_):
    best = 0
    val1 = 0
    if depth == 0:
        return evaluate(board)
    elif turn == "white":
        for move in all_moves(board ,"2"):
            new_board = board.copy()
            move_piece(move , new_board)
            val = minimax(new_board , "black", alpha , beta,depth-1 ,0)
            best = move if val > alpha else best
            alpha = max(alpha , val)
            val1 = alpha
            if beta <= alpha :
                break
    elif turn == "black":
        for move in all_moves(board, "1"):
            new_board = board.copy()
            move_piece(move , new_board)
            val = minimax(new_board , "white", alpha , beta,depth-1 ,0)
            best = move if val < beta else best
            beta = min(beta , val)
            if beta <= alpha :
                break
            val1 = beta
    if return_ == 1:
        return best
    elif return_ == 0:
        return val1

# calculating the centi-pawns for every side :

def cal_pts(board2):
    white_pts = 0
    black_pts = 0
    for x in board2:
        for y in x:
         if y[0] == "1":

                 white_pts =  white_pts+1 if y[1] == 'p' else white_pts
                 white_pts = white_pts+3 if y[1] == 'n' else white_pts
                 white_pts = white_pts+3 if y[1] == 'b' else white_pts
                 white_pts = white_pts+5 if y[1] == 'r' else white_pts
                 white_pts = white_pts+9 if y[1] == 'q' else white_pts
                 white_pts = white_pts+1000 if y[1] == 'k' else white_pts
         elif y[0] == "2":
                 black_pts = black_pts+1 if y[1] == 'p' else black_pts
                 black_pts = black_pts+3 if y[1] == 'n' else black_pts
                 black_pts = black_pts+3 if y[1] == 'b' else black_pts
                 black_pts = black_pts+5 if y[1] == 'r' else black_pts
                 black_pts = black_pts+9 if y[1] == 'q' else black_pts
                 black_pts = black_pts+1000 if y[1] == 'k' else black_pts
    return  white_pts - 1000 , black_pts - 1000

def evaluate(board3):
    w_pts , b_pts = cal_pts(board3)
    exig1 = w_pts - b_pts

    return exig1

# moving the pieces:

def move_piece(notation , board1):
   #print(notation)
   x , y = C[notation[0]] , int(notation[1]) - 1
   z , e = C[notation[2]] , int(notation[3]) - 1
   board1[7-e , z] = board1[7 - y , x]
   board1[7-y , x] = "   " 

def show_board(board_list):
    print("")
    for i , x in enumerate(board_list):
       line = str(8 - i) + " # "
       for y in x:
          
          line += "  " + y[0:2] + "  "
       print(line)
       print("")
    print("      " + "#     "*8)
    print("      a     b     c     d     e     f     g     h")    
             
           
             


def simulation(board5, turn, depth):
    new_board = board5.copy()
    while True:
        time_start = time.time()
        print("best move for white based on KnightMare Bot >>> 1-",minimax(new_board ,turn, -10000 , 10000,depth,1))
        print(f"Processing duration : {round(time.time() - time_start , 2)} s")
        wmove_ins = input("Your move (white) ------> ")
        move_piece(wmove_ins , new_board)
        bmove_ins = input("Your move (black) ------> ")
        move_piece(bmove_ins , new_board)
        show_board(new_board)
        print(cal_pts(new_board))

def game(board7, depth):
    new_board = board7.copy()
    n = 0
    while True:
        show_board(new_board)
        wmove_ins = input("Your move (white) ------> ")
        move_piece(wmove_ins , new_board)
        time_start = time.time()
        bk_move = minimax(new_board ,"black", -10000 , 10000,depth,1) if n > 2 else kings_indian[n]
        n += 1
        print(f"Processing duration : {round(time.time() - time_start , 2)} s")
        move_piece(bk_move , new_board)     
        print(cal_pts(new_board))
        
def home():
    print( '# Play chess against KnightMare ( 800 rated bot)')
    print("NB: you can only play as white")
    choice = input("1_ baby mode \n2_ normal mode  \n3_ hard mode  \n(1/2/3) -----> ")
    if choice =="1":
        game(board , 2)
    
    if choice =="2" :
        game(board,4)
        
    else:
        game(board,6)
     
home()
