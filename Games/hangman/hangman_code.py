from calendar import c
import random 
from hangman import hangman 

words=["python","css","java","html"]
word=random.choice(words)

def game_on(word):
    guss_word=["_" for i in word]
    tries=0
    print(hangman[tries])
    print("Guess the Word : {}".format(guss_word))
    while True:
        letter=input("Enter the letter : ")
        if not letter.isalpha():
            print("Please enter alphabets only : ")
        if letter in word:
            word_list=[i for i in range(len(word)) if word[i]==letter]
            for index in word_list:
                guss_word[index]=letter
            print("*"*50)
            print("You guessed the correct letter in the word : {}".format(guss_word))

            if "".join(guss_word)==word:
                return "You guessed the word "
        else:
            tries+=1
            print(hangman[tries])
            if tries==6:
                return "game over you loss the game"
            print("Sorry! Try Again : {}".format(guss_word))
                   

if __name__=='__main__':
    while True :
        print(game_on(word))
        play_again=input("Do you want to play again print [y/n] : ")
        if play_again=="y":
            word=random.choice(words)
            continue 
        else:
            print("Bye")
            break
