"""
Pedro Cruz
cookie_jar.py
"""

def welcome():
    print("========================================")
    print("Welcome to the Cookie Jar game!")
    print()
    print("Whoever takes the last cookie has to go buy more,"\
    " so the objective\nof the game is to take as many cookies as "\
    "you can without being the\none who takes the last cookie. "\
    "You also can't take more than three\ncookies at a time,"\
    " since that's just rude.")
    print("========================================")

def is_valid(choice, min_val, max_val):
    choice = int(choice)
    if ((choice >= min_val) and (choice <= max_val)):
        return True
    s = "Sorry, you can't take %d cookies; value must be between " % (choice)
    s = s + "%d and %d." % (min_val, max_val)
    print(s)
    return False

def get_choice(min_val, max_val, player, cookies):
    choice = input("How many cookies does %s want to take? " % (player))
    while (not choice.isdigit()):
        s = "Sorry, you can't take %s cookies; " % (choice)
        s = s + "value must be an integer."
        print(s)
        choice = input("Please enter a value between 1 and %d: " % (max_val))
    while (not (is_valid(choice, min_val, max_val)) or int(choice) > cookies):
        choice = input("Please enter a value between 1 and %d: " % (max_val))

    return int(choice)

def print_status(player, current_turn, cookies_left):
    print("----------")
    print("Turn %d - Jar contains %d cookies" % (current_turn, cookies_left))
    print("It's %s's Turn" % (player))

def get_player(current_turn, players):
    next_to_play = current_turn % len(players)
    return players[next_to_play]

def game_over(winner, loser):
    print()
    print("### The cookie jar is empty! ###")
    print("%s takes the last cookie and must go buy another box!" % (loser))
    print("%s wins!" %(winner))

def play_game(players, min_take, max_take, cookies):
    turn = 0
    while (cookies > 0):
        current_player = get_player(turn, players)
        print_status(current_player, turn, cookies)
        choice = get_choice(min_take, max_take, current_player, cookies)
        cookies = cookies - choice
        turn += 1
        if (cookies < 3):
            max_take = cookies

    if (current_player == players[0]): 
        winner = players[1]
    else: 
        winner = players[0]
    game_over(winner, current_player)

def main():
    welcome()

    players = ["a", "b"]

    players[0] = input("What is the first player's name? ")
    players[1] = input("What is the second player's name? ")

    play_game(players, 1, 3, 12)

main()
