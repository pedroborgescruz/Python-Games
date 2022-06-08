"""
Five-Six-Seven Game.
Author: Pedro Cruz
Februrary, 2022
"""
from random import *

def main():
    name = input("Enter your name: ")
    printWelcome(name)
    print("Enter the number of rounds you'd like to play (up to 30 max):")
    num_plays = getNumBetween(1, 30)
    wins = 0

    for i in range(num_plays):
        print()
        print("Let's start round %d..." %(i+1))
        winner = playOneRound(name)
        if winner == 1:
            wins += 1
   
    print()
    printResults(wins, num_plays, name)

def getNumBetween(low, high):
  
    num = int(input("Enter a value between %d and %d: " %(low, high)))
    while (num < low) or (num > high):
        print("hey, %d is not between %d and %d. try again..." %(num,low,high))
        num = int(input("Enter a value between %d and %d: " %(low, high)))

    return num

def printWelcome(username):
    print("Hi, %s, and welcome to the game of 5-6-7!" %(username))
    print("Each round you pick a number between 0 and 5 inclusive")
    print(" and the computer picks a number between 0 and 5 inclusive.")
    print("If the total of the two values is between 5 and 7 inclusive,")
    print(" you win! If not, the computer wins. :(")
    print("At the end of all the rounds, I'll print out your win percentage.")
    print()
    print("Good luck!")
    print()

def printResults(user_wins, num_rounds, username):
    comp_wins = num_rounds - user_wins 
    print("%s, you won %d out of %d" %(username, user_wins, num_rounds))
    print("for a winning percentage of %.2f" %(user_wins/num_rounds))
    
    if user_wins > comp_wins:
        print("You beat the computer. Yay!")
    else: 
        print("The computer beat you. Better luck next time!")

def playOneRound(username):
    print("%s, you get to start this round by picking a number." %(username))
    user_choice = getNumBetween(0, 5)
    comp_choice = randrange(0, 5)
    x = user_choice + comp_choice

    print(" you picked %d and computer picked %d" %(user_choice, comp_choice))

    if (x==5) or (x== 6) or (x==7):
        print(" You win this round!")
        return 1 #user wins
    else:
        print(" Sorry, you lose this round!")
        return 0 #computer wins  

main()
