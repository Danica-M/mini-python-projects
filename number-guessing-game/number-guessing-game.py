import random
import math

def play():
    #generating a random number from 1 to 100
    number = random.randint(1,100)

    #welcome message
    print("You have 5 attempts to guess the number correctly!")

    #counts the number of attempts
    attemptCounter = 0

    #checks is the guess is the correct number
    while attemptCounter < 5:
        playerGuess= int(input("Your Guess: "))
        if number == playerGuess:
            print("Congratulation you guessed it correctly on your ",attemptCounter +1," attempt!")
            break
        elif number > playerGuess:
            print("Higher")
        elif number < playerGuess:
            print("Lower")
        attemptCounter+=1

    #Check if player has finish the number of attempts
    if attemptCounter >=5:
        print("The correct number is ",number,". Better luck next time!")
        


#gives the player the option to keep playing the game 
while True:
    play()
    playAgain = str(input("do you want to play again? Y/N: "))
    if playAgain.upper() == "N":
        break
