"""
This program simulates a digital version of the game Odds and Even.

Author: Pedro Cruz
09/28/2021
"""

def predict_it():
    """
    The purpose of this function is to prompt the user for their prediction and
    check whether what they entered is a valid response or not. After doing so,
    this function returns the value to the following one.

    No input parameters collected for this function.
    """

    prediction = input("Predict either odd or even: ")

    while prediction != "even" and prediction != "odd":
        print()
        print("Whoops, you must predict either odd or even. Try again.")
        prediction = input("Predict either odd or even: ")

    return prediction

def get_choice():
    """
    The purpose of this function is to prompt the user for an integer
    between 0 and 5  whether what they entered is a valid response or not. After
    doing so, this function returns the value to the following one.

    No input parameters collected for this function.
    """
    print()
    user_vl = input("Enter a number between 0 and 5: ")

    while (user_vl.isdigit() == False) or int(user_vl)<0 or int(user_vl)>5:
        print()
        print("Sorry, you must enter an integer between 0 and 5.  Try again.")
        user_vl = input("Enter a number between 0 and 5: ")

    return int(user_vl)

def determine_winner(prediction, user_choice, comp_choice):
    """
    The purpose of this function is to determine the winner of the round. After
    doing so, this function returns the boolean value to the following one.

    Input parameters collected for this function are prediction, user_vl, and
    comp_choice.
    """

    sum_values = int(user_choice) + comp_choice

    if (prediction == "odd"):
        if (sum_values%2 == 0):
            result = False

        else:
            result = True

    elif (prediction == "even"):
        if (sum_values%2 == 0):
            result = True

        else:
            result = False

    return result

def print_scores(name, user_wins, comp_wins):
    """
    The purpose of this function is to print the scores of the oponents after
    each round.

    Input parameters collected for this function are name (name of the user),
    user_wins (number of wins of the user), and comp_wins (number of wins of
    the computer).
    """

    print("------------------------------")
    print("%s: %i      Computer: %i" %(name, user_wins, comp_wins))
    print("------------------------------")

def main():
    import random

    user_name = input("Hi! I'm excited to play against you. What's your name? ")
    num_rounds = int(input("Ok, %s, how many rounds do you " %(user_name) +
    "want to play? "))
    user_wins = 0
    comp_wins = 0

    for i in range(num_rounds):
        prediction = predict_it()
        user_choice = get_choice()
        comp_choice =  random.randint(0, 5)

        print("%s predicts %s and " %(user_name, prediction) +
        "chooses %d." %(user_choice))
        print("Computer chooses %d." %(comp_choice))
        result = determine_winner(prediction, user_choice, comp_choice)

        if result == True:
            user_wins = user_wins + 1
            print("  %s wins!" %(user_name))

        else:
            comp_wins = comp_wins + 1
            print("  Computer wins!")

        print_scores(user_name, user_wins, comp_wins)

    if user_wins>comp_wins:
        print("The champion is: %s!" %(user_name))
    elif comp_wins>user_wins:
        print("The champion is: Computer!")
    else:
        print("The final score is a tie!")

main()
