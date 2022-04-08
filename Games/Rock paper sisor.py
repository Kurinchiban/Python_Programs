# Rock Paper scissors
from ast import While
import random
def P1():
    list_1=["R","P","S"]
    computer=random.choice(list_1)
    print("Computer chooses : {} ".format(computer))
    if computer=="R":
        print("Computer chooses : Rock")
    
    elif computer=="P":
        print("Computer chooses : Paper")
    else:
        print("Computer chooses : Scissors")
    return computer
def P2():
    player=input("Enter Rock Paper or Scissors as R/P/S : ").upper()
    if player=="R":
        print("Player chooses : Rock")
    
    elif player=="P":
        print("Player chooses : Paper")
    else:
        print("Player chooses : Scissors")
    return player

def root(player,computer):
    if (player=="R" or player=="P" or player=="S"):   

        if computer==player:
            print("Both players are selected same the game is TIE")

        elif player=="R":
            if computer=="P":
                print("Paper covers rock! Computer won")
            else:
                print("Rock smashes scissors! You won")

        elif player=="P":
            if computer=="R":
                print("Paper covers rock! You won")
            else:
                print("Scissors cuts paper! Computer won")

        elif player=="S":
            if computer=="R":
                print("Rock smashes scissors! Computer won")
            else:
                print("Scissors cuts paper! You won")
    else:
        print("Enter the valid Input R/P/S:")

print("Let's Play game")

while True:
    play_game=input("Are you readey to play print yes or no : ").upper()
    if play_game=="YES":
        game_on=True 
    else:
        print ("Bye")
        break
    while game_on:
        b=P2()
        a=P1()
        c=root(b,a) 
        break
    
