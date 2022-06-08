"""
In this game, the computer generates a secret "code", which is a list of four
colors e.g. "green green blue red". There are six possible colors: red, yellow,
blue, green, orange, and purple.

The object of the game is to win. The player wins by guessing the secret code.
Each turn, the player enters a guess for the code e.g. "blue orange yellow
blue". The computer then reports how many exact matches the player had, and how
many inexact matches the player had. An inexact match is when the player guesses
the color correctly, but not the position, and an exact match is when the player
guesses a color correctly and puts it in the correct position.

The player has ten turns to guess the secret code. If they do, they win!
Otherwise, the computer wins.

Author: Pedro Cruz
October 2021
"""

def print_colors(color_list):
    print(color_list)

def get_guess(colors):
    """
    This function asks for the user to enter four colors and checks if they are
    valid input options. Parameter "colors" (the list of valid colors) is
    required.
    """

    colors_guessed = []

    print("Please enter four legal colors. Your choices are: red, orange, "+
    "yellow, green, blue, purple.")

    for i in range(1,5):
        guess = input("Enter color %d: "%(i))

        while guess not in colors:
            print()
            print("%s is not a valid color."%(guess))
            guess = input("Please choose from the following colors: red, " +
            "orange, yellow, green, blue, purple: ")

        colors_guessed.append(guess)

    return colors_guessed

def generate_code(colors):
    """
    This function generates the secret code that the user needs to guess.
    Parameter "colors" (the list of valid colors) is required.
    """
    from random import choice

    secret_code = []

    for i in range(4):
        color = choice(colors)
        secret_code.append(color)

    return secret_code

def exact_matches(secret_code, guess, status):
    """
    This function compares the user's guess and the secret code in order to
    determine the number of exact matches, i.e. how many correct colors are in
    the correct position. Parameters "secret_code" (the game's secret code),
    "guess" (the colors entered by the user), and "status" (a list that will be
    later given as feedback to the user) are required.
    """

    exact_matches = 0

    for i in range(4):
        if guess[i] == secret_code[i]:
            status[i] = "exact"
            exact_matches += 1

    return exact_matches

def inexact_matches(secret_code, guess, status):
    """
    This function compares the user's guess and the secret code in order to
    determine the number of inexact matches, i.e. how many correct colors are in
    the wrong position. Parameters "secret_code" (the game's secret code),
    "guess" (the colors entered by the user), and "status" (a list that will be
    later given as feedback to the user) are required.
    """

    inexact_matches = 0

    for i in range(4):
        if status[i] != "exact":
            for j in range(4):
                if guess[i] == secret_code[j]:
                    if status[j] == "":
                        inexact_matches += 1
                        status[j] = "inexact"

    return inexact_matches

def print_introduction():
    """
    This function prints the instructions of the game to the user. No parameters
    required.
    """
    print("""
    Welcome to Mastermind!

    Your goal is to guess a sequence of four colors.
    Each color can be blue, green, red, orange, purple, or yellow.
    Then I'll tell you how many times you guessed the correct color
        in the correct position, and how many times you guessed the
        correct color, but in the wrong position.

    You have ten turns to guess the correct sequence.
    Good luck!
    """)

def is_game_over(num_exact_matches, turn):
    """
    This function checks the conditions for the game to end and returns 'True'
    in case they are met. Parameters "num_exact_matches" (the number of exact
    matches between the secret code and the user's guess) and "turn" (the
    current turn of the game) are required.
    """

    game = False

    if (num_exact_matches == 4) or (turn == 11):
        game = True

    return game

def player_won(num_exact_matches):
    """
    This function checks the condition for the user to win the game and returns
    'True' in case it is met. Parameter "num_exact_matches" (the number of
    exact matches between the secret code and the user's guess) is required.
    """

    won = False

    if num_exact_matches == 4:
        won = True

    return won

def main():
    """
    Here, we are putting the pieces together and structuring our game by passing
    arguments along to the called functions. No parameters required for 'main.'
    """
    color_list = ["red", "orange", "yellow", "green", "blue", "purple"]

    print_introduction()
    code = generate_code(color_list)
    print(code)
    turn = 0

    for i in range(1,11):
        status = ["","","",""]
        print()
        print("Turn %s:"%(i))
        userGuess = get_guess(color_list)
        exactMatches = exact_matches(code, userGuess, status)
        inexactMatches = inexact_matches(code, userGuess, status)

        print()
        print("You guessed:")
        print(*userGuess,sep = ", ")

        if exactMatches == 1:
            print("There is %d exact match." %(exactMatches))
        else:
            print("There are %d exact matches." %(exactMatches))

        if inexactMatches == 1:
            print("There is %d inexact match." %(inexactMatches))
        else:
            print("There are %d inexact matches." %(inexactMatches))

        turn += 1

        if is_game_over(exactMatches, inexactMatches) == True:
            break

    if player_won(exactMatches) == True:
        print()
        print("The answer was:\n%s.\n\nYou won!"%(code))
        if turn == 1:
            print("It took you %d turn to get the correct answer."%(turn))
        else:
            print("It took you %d turns to get the correct answer."%(turn))

    else:
        print()
        print("Time's up! Sorry, buddy :(\n\nThe answer was:")
        print(*code,sep = ", ")
        print("\nTry playing again until you defeat me ;)")

main()
