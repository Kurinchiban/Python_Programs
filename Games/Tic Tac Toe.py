# Tic Tac Toe Game
# Step 1 :Diaplay a Board 
# step 2 :assigning the value x and o to the player
# step 3 :assigning who play first
# step 4 :placing the marker to the board
# step 5 :space check
# step 6 :full board check
# step 7 :player choise
# step 8 :win check
# step 9 :re-play the game or not 
# step 10:organize the code 

# diven code

import random
from re import X
def Display(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
"""

board=["x","x","x","x","x","x","x","x","x","x"]
Display(board)
"""
def player_input():
    marker=""
    while not (marker=="X" or marker=="O"):
        marker=input("player 1 please enter X or O : ").upper()
    if marker=="X":
        return ("X","O")
    else:
        return ("O","X")
"""
p1,p2=player_input()
print(p1)
print(p2)
"""
def choose_first():
    if random.randint(0,1)== 0:
        return "player 2"
    else:
        return "player 1" 

def place_marker(board,marker,position):
    board[position]=marker

"""
test_board=["x","x","x","x","x","x","x","x","x","x"]
place_marker(test_board,"#",8)
Display(test_board)
"""
def space_check(board,position):
    return board[position]==" " # will return boolean

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False 
    return True
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose the position (1-9) : "))
    return position

def win_check(board,mark):

    return((board[1]==mark and board[2]==mark and board[3]==mark) or 
    (board[4]==mark and board[5]==mark and board[6]==mark) or
    (board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[1]==mark and board[5]==mark and board[9]==mark) or
    (board[7]==mark and board[5]==mark and board[3]==mark) or
    (board[1]==mark and board[4]==mark and board[7]==mark) or
    (board[2]==mark and board[5]==mark and board[8]==mark) or
    (board[3]==mark and board[6]==mark and board[9]==mark))
    
def replay():
    choice=input("Will you play again please enter yes or no").upper()
    return choice=="YES"
  
print("welcome to the Tic Tac Toe game let's play...")

while True:
    #play Game 
    #set board,markerand who is first
    the_board=[" "]*10
    player_1_marker,player_2_marker=player_input()
    turn=choose_first()
    print(turn + "will go first")
    play_game=input("Are you readey to play print yes or no : ").upper()
    if play_game=="YES":
        game_on=True 
    else:
        game_on=False 
    while game_on:
        #player1
        if turn=="player 1":
            Display(the_board)
            position=player_choice(the_board)
            print(position)
            place_marker(the_board,player_1_marker,position)
            if win_check(the_board,player_1_marker):
                Display(the_board)
                print("Player 1 you WON the game")
                game_on=False 
            else :
                if full_board_check(the_board):
                    Display(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn="player 2"
        else:
            Display(the_board)
            position=player_choice(the_board)
            print(position)
            place_marker(the_board,player_2_marker,position)
            if win_check(the_board,player_2_marker):
                Display(the_board)
                print("Player 2 you WON the game")
                game_on=False 
            else :
                if full_board_check(the_board):
                    Display(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn="player 1"
    if not replay():
        break
