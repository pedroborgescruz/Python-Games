"""
Melty — a freezing alternative to the classic 'Hangman' game.
Author: Pedro Cruz
March 2022
"""
from random import *

def main():
    printWelcome()
    word = generateWord("/usr/local/doc/wordfile.txt")
    totalLeft = 8
    puzzle = generatePuzzle(word)
    guessedLetters = []

    while (not isGameOver(totalLeft, puzzle)):
        print()
        printMelty(totalLeft)
        printPuzzle(puzzle)
        print("incorrect guesses left: %d" %(totalLeft))
        userGuess = getGuess(guessedLetters)
        printFeedback(userGuess, word)
        puzzle = updatePuzzle(userGuess, puzzle, word)
        totalLeft = guessesLeft(userGuess, word, totalLeft)

    printResult(puzzle, word)

def printWelcome():
    """
    Purpose: This function prints the intro message.
    Parameters: None.
    Return: None.
    """
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("This program plays a game of Melty.")
    print()
    print("Guess letters in the mystery word.\nYou can only make 8 incorrect \
    guesses before Melty melts.\nSee if you can save Melty and guess the \
    word before you run out of guesses.\n")
    print("              Good Luck!")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def printMelty(leftGuesses):
  """
  This functions prints the status of the snowman based on the number of 
    guesses left.
  Parameters: leftGuesses (type: int).
  Return: None.
  """
    if leftGuesses == 8:
        print("""         
     __
   _|==|_  
    ('')___/
>--(`^^')
  (`^'^'`)
  `======' 
        """)
    elif leftGuesses == 7: 
        print(""" 
    ('')___/
>--(`^^')
  (`^'^'`)
  `======'
        """)

    elif leftGuesses == 6:
        print("""
    ('')
>--(`^^')
  (`^'^'`)
  `======' 
        """)

    elif leftGuesses == 5:
        print("""  
    ('')
   (`^^')
  (`^'^'`)
  `======' 
        """)
    
    elif leftGuesses == 4:
        print("""  
    ('')
   (`^^')
  (`^'^'`)
        """)

    elif leftGuesses == 3:
        print("""  
    ('')
   (`^^')
        """)

    elif leftGuesses == 2:
        print("""  
    ('')
        """)

    else:
        print("""  
    (  )
        """)


def getGuess(guessedLetters):
    """
    Purpose: This function gets the guess from the user.
    Parameters: guessedLetters - list containing letters already guessed.
    Return: "guess" - the user's guess.
    """
    guess = input("Enter a letter: ")

    while (guess.isdigit()) or (len(guess) > 1) or (guess in guessedLetters):
        if (len(guess) > 1):
            print(" sorry, honey. you can only pass one letter at a time\n \
                let's try again!")
            guess = input("Enter a letter: ")
        elif (guess.isdigit()):
            print(" sorry, hun. no numbers allowed, only letters! :/")
            guess = input("Enter a letter: ")
        elif guess in guessedLetters:
            print(" sorry, babes! you already guessed that one. try again :)")
            guess = input("Enter a letter: ")
    
    guessedLetters.append(guess)

    return guess.lower()

def generateWord(file):
    """
    Purpose: This function randomly selects a word from a file to serve as
        the secret code to be guessed.
    Parameters: None.
    Return: "word" - secret word.
    """
    infile = open(file, "r")
    lines = infile.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        lines[i] = line

    infile.close()

    word = choice(lines)

    return word

def generatePuzzle(secretWord):
   """
   Purpose: This function generates the word puzzle.
   Parameters: "secretWord" - the secret code to be guessed.
   Return: "puzzle" - list containing word in dashes.
   """
   puzzle = []

   for i in range(len(secretWord)):
       puzzle.append("_")

   return puzzle

def printPuzzle(puzzle):
    """
    Purpose: This function prints out the puzzle to the user.
    Parameters: "puzzle" - a list containing the elements of the puzzle.
    Return: None.
    """
    toPrint = ""
    
    for i in range(len(puzzle)):
        toPrint += (puzzle[i])
        if i != len(puzzle):
            toPrint += " "

    print("word: " + toPrint)

def updatePuzzle(guess, puzzle, secretWord):
    """
    Purpose: This function updates the word as the user guesses letters
         correctly.
    Parameters: "letter" - the letter guessed by the player - and "secretWord" -
(guess.isdigit()) or (len(guess) > 1)         the secret code to be guessed.
    Return: "puzzle" - word in the current stage (type: list).
    """
    word = list(secretWord)
    position = []

    for i in range(len(secretWord)):
        if guess == word[i]:
            position.append(i)

    for j in range(len(position)):
        puzzle[position[j]] = guess

    return puzzle

def printFeedback(letter, code):
    """
    Purpose: This function lets the user know if the letter in present
        in the secret word or not.
    Parameters: "letter" - the letter guessed by the player - and "code" -
        the secret code to be guessed.
    Return: None.
    """
    word = list(code)

    if letter not in word:
        print(" sorry there is no '%s' in the word." %(letter))
    else:
        print(" good guess, '%s' is in the word." %(letter))

def guessesLeft(letter, code, guessesLeft):
    """
    Purpose: This function computes how many incorrect guesses the player
        still has available.
    Parameters: "letter" - the letter guessed by the player -, "code" -
        the secret word to be guessed -, and "guessesLeft" - number of incorrect
        guesses left currently.
    Return: "guessesLeft" - how many guesses are still left.
    """
    word = list(code)

    if (letter not in word):
        guessesLeft = guessesLeft - 1

    return guessesLeft

def isGameOver(guessesLeft, puzzle):
    """
    Purpose: This function checks if the game is over.
    Parameters: "guessesLeft" - the number of incorrect guesses left - and
        "puzzle" - the puzzle with guessed letters filled.
    Return: True - if game isn't over - or False - if game is over.
    """
    if (guessesLeft == 0) or ("_" not in puzzle):
        return True
    return False

def printResult(puzzle, word):
    """
    Purpose: This function prints out the final result of the game.
    Parameters: "word" - the secret word to be guessed -, and
        "guessesLeft" - the number of incorrect guesses available.
    Return: None.
    """
    print()
    if ("-" in puzzle):
        print("    ... I've melted!  :(")
        print("Sorry, Melty melted. The word was: %s" %(word))
        print("Better luck next time!")
    else:
        print("You won!!! The word was: %s. You saved Melty!" %(word))

main()
        
