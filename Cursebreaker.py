"""
Cursebreaker game.
Author: Pedro Cruz
February 2022
"""
from random import *

def main():
    vldRunes = ["ansuz","isaz","sowilo","hagalaz","algiz","ehwaz","naudiz"]
    secretCode = ["", "", "", ""]
    userChoice = []
    generate_code(vldRunes, secretCode)
    keep_going = True
    turn = 1
    print_introduction()
    while keep_going:
        print("============\nTurn %d" %(turn))
        get_guess(vldRunes, userChoice)
        print()
        print("You guessed:")
        print_runes(userChoice)
        matches = check_guess(secretCode, userChoice)
        print("%d / 4 correct" %(matches))
        if is_game_over(matches, turn) == True:
            keep_going = False
            if player_won(matches) == True:
                print()
                print("Congratulations, you win! The curse is broken!")
            else:
                print()
                print("Sorry you lost; good thing there's a big stack of " +
                        "cursed artifacts!")
        else:
            userChoice = []
            turn += 1

def print_runes(rune_list):
    """
    Purpose: Format list of runes and print it back to user.
    Parameters: rune_list (a list containing a sequence of runes.)
    Return: None.
    """
    to_print = "|"

    for i in rune_list:
        to_print += (" " + i + " |")

    print(to_print)

def get_rune(runes, number):
    """
    Purpose: Prompt user for a rune and validate if it's a legal entry.
    Parameters: runes (list of valid runes) and number (integer indicating
        current rune.) 
    Return: rune (string; user entry.)
    """
    rune = input("Enter rune %d: " %(number))
    while rune not in runes:
        print(rune + " is not a valid rune; please choose from the " + 
            "following runes:")
        print_runes(runes)
        rune = input("Enter rune %d: " %(number))
        
    return rune 

def get_guess(runes, guess):
    """
    Purpose: Get all four user guesses and store them in a list of guesses.
    Parameters: runes (list of valid entries) and guess (list to store user 
        entries.)
    Return: None.
    """
    print("Please enter four legal runes. Your choices are:")
    print_runes(runes)

    for i in range(4):
        rune = get_rune(runes, i+1)
        guess.append(rune)

def generate_code(runes, code):
    """
    Purpose: Generate the secret code to be broken by the player. 
    Parameters: runes (list of valid entries) and code (empty list in which
        the secret code will be stored.)
    Return: None.
    """
    done = False
    counter = 0

    while not done:
        item = choice(runes)
        if item not in code:
            code[counter] = item
            counter += 1 
        if counter == 4:
            done = True

def check_guess(code, guess):
    """
    Purpose: Compare secret code and the user choices to evaluate if they
        match exactly.
    Parameters: code (list containing the runes that form the secret code) 
        and guess (list of user-chosen runes.)
    Return: matches (int; number of runes that match exactly.)
    """
    matches = 0
    for i in range(4):
        if guess[i] == code[i]:
            matches += 1

    return matches

def print_introduction():
    """
    Purpose: Helper function that prints out the instructions of the game.
    Parameters: None.
    Return: None.
    """
    print("Welcome to Curse Breaker!")
    print(" The object of the game for the player is to guess the rune " +
            "sequence,\ne.g. sowilo isaz halaz ansuz. For our game, we'll " +
            "use 4 runes in\nthe sequence, and we'll say each rune can only " +
            "show up once (i.e.\nthere are no duplicates in the sequence). " +
            "Each turn, the player\nenters a guess, and the program then " + 
            "reports how many of the player's\nguesses are correct (using " +
            "exact matches, meaning the right rune in\nthe right place).")
    print()
    print("The player has thirteen turns to guess the secret code. If they " +
            "do,\nthey win! Otherwise, the artifact explodes and the evil " +
            "wizard wins!")
    print()

def is_game_over(num_matches, turn):
    """
    Purpose: Evaluate if the game is over or not  by checking if (1) the user
        got all the items of the code exactly right or (2) the number of turns
        is over.
    Parameters: num_matches (int; number of exact matches between code and user 
        choices) and turn (number of current turn).
    Return: Boolean; 'True' if game is over and 'False' if game is still not 
        over.
    """
    if (num_matches == 4) or (turn == 13):
        return True
    else:
        return False

def player_won(num_matches):
    """
    Purpose: Check if player has won the game.
    Parameters: num_matches (int; number of exact matches between code and user
        choices.)
    Return: 'True' if user has won.
    """
    if num_matches == 4:
        return True

main()
