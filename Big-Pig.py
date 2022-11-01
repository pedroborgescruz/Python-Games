'''
Pedro Cruz
big-pig.py
'''
import random

def printInstructions() -> None:
    """
    This function prints the instructions of the game to the console.
    @parameters: 
        none.
    @return:
        none.
    """
    print("Welcome to Big Pig, the dice rolling game where players try to be "\
    "the first get 100 points! Players (you and the computer) will take turns "\
    "rolling two dice as many times as they want, adding all roll results to "\
    "a running total. Players lose their gained score for the turn if they "\
    "roll a 1.")
    
def printStatus(human: int, computer: int) -> None:
    """
    This functions prints the current scoreboard of the players to the console.
    @parameters:
        human (int) - current score of human player
        computer (int) - current score of computer player
    @return:
        none.
    """
    print()
    print("--------------------------------------------------")
    print("Player has %d and computer has %d." %(human, computer))
    
def getUserChoice() -> str:
    """
    This function gets the user input for the current turn. User can choose 
        to either [r]oll the dice - keep playing for the turn - or [h]old
        the dice - save points from the current turn to game score.
    @parameters:
        none.
    @return:
        choice (string) - user input; either [r]oll or [h]old.
    """
    choice = input("What do you want to do: [r]oll or [h]old? ")
    
    while (not isValid(choice)):
        choice = input("What do you want to do: [r]oll or [h]old? ")

    return choice

def isValid(choice: str) -> bool:
    """
    This function checks whether the user input is valid.
    @parameters:
        choice (string) - user's choice.
    @return:
        boolean; True if @choice is valid or False if @choice is not valid.
    """
    valid = ["r", "h", "hold", "roll"]
    if choice not in valid:
        return False
    return True

def printRoll(name: str, dice: list, pts: int) -> None:
    """
    This function prints the roll outcomes.
    @parameters:
        name - (str) player who rolled.
        diceValuces - (list) values of the dice.
        score - (int) total round score.
    @return:
        none.
    """
    print("%s rolled [%d, %d], current round score: %d"%(name, dice[0], dice[1], pts))

def rollDice()-> 'list':
    """
    This function randomly rolls two dice.
    @parameters:
        none.
    @return:
        List; values of random dice rolling.
    """
    diceOne = random.randrange(1,7)
    diceTwo = random.randrange(1,7)

    return [diceOne, diceTwo]
    
def rollUpdate(diceValues: 'list') -> int:
    """
    This function computes the score of the player based on the values of 
        their dice.
    @parameters: 
        diceValues (list) - the values of the dice after rolling.
    @return: 
        diceScore (int) - the score associated with the values of the dice. 
        It can be:
            a. 0 if the player rolls a 1 on one die and anything except a
                1 on the other die;
            b. (diceValues[0] + diceValues[1]) if the player rolls two different
                values on their dice;
            c. 25 if the player rolls a 1 on both dice;
            d. (2 * (diceValues[0] + diceValues[1])) If the player rolls the 
                same value on both dice (and that value is greater than 1).
    """
    diceScore = 0
    
    if (diceValues[0] == 1 and diceValues[1] == 1):
        diceScore = 25
    elif (1 in diceValues):
        diceScore = 0
    elif (diceValues[0] != diceValues[1]):
        diceScore = (diceValues[0] + diceValues[1])
    else:
        diceScore = 2*(diceValues[0] + diceValues[1])
        
    return diceScore
    
def isGameOver(human: int, computer: int) -> bool:
     """
     This function determines whether the game is over or not. The game ends
        when one of the players score at least 100 points.
    @parameters:
        human (int) - current score of human player
        computer (int) - current score of computer player
    @return:
        boolean; True if game is over or False is should continue playing.
     """
     if (human >= 100 or computer >= 100):
         return True
     return False

def printGameResults(human: int, computer: int) -> None:
    """
    This function prints the final results of the game, announcing the winner
        alongside the final scoreboard.
    @parameters: 
        human (int) - current score of human player
        computer (int) - current score of computer player
    @return:
        none.
    """
    winner = "Computer"
    if human > computer:
        winner = "Human"
    print()
    print("%s wins [%d, %d]!" %(winner, human, computer))

def playComputerGame(human: int, computer: int) -> int:
    """
    This function simulates one turn played by the computer.
    @parameter:
        human (int) - current score of human player
        computer (int) - current score of computer player
    @return:
        turnResult (int) - the result of the turn played by the computer.
    """
    turnScore = 0
    
    if human < 100:
        while (turnScore < 20):
            myDice = rollDice()
            rollResult = rollUpdate(myDice)
            if (rollResult == 0):
                turnScore = 0
                printRoll("computer", myDice, turnScore)
                print("Big pig!")
                break
            turnScore += rollResult
            printRoll("computer", myDice, turnScore)
    else:
        while (computer < human):
            myDice = rollDice()
            rollResult = rollUpdate(myDice)
            if (rollResult == 0):
                turnScore = 0
                printRoll("computer", myDice, turnScore)
                print("Big pig!")
                break
            turnScore += rollResult
            printRoll("computer", myDice, turnScore)

    return turnScore
             
def playUserGame(human: int, computer: int) -> int:
    """
    This functions plays one turn of the game.
    @parameters:
        human (int) - current score of human player
        computer (int) - current score of computer player
    @return:
        turnScore (int) - the score of the turn played by the user.
    """
    turnScore = 0
    choice = getUserChoice() 
    
    while (choice not in ["hold", "h"]):
        myDice = rollDice()
        rollResult = rollUpdate(myDice)
        if (rollResult == 0):
          turnScore = 0
          printRoll("human", myDice, turnScore)
          print("Big pig!")
          break
        turnScore += rollResult
        printRoll("human", myDice, turnScore)

        choice = getUserChoice() 

    return turnScore
    
def main():
    userScore = 0
    computerScore = 0
    printInstructions()
    
    while (not (isGameOver(userScore, computerScore))):
        printStatus(userScore, computerScore)
        userScore += playUserGame(userScore, computerScore)
        printStatus(userScore, computerScore)
        computerScore += playComputerGame(userScore, computerScore)
        
    printGameResults(userScore, computerScore)
    
main()
