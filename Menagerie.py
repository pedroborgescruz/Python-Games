"""
Menagerie - an alternative to Tamagotchi.
Author: Pedro Cruz
April, 2022
"""

from critter import *

def main():
    my_critters = []
    menu()
    choice = get_choice()
    print()
    while (choice != 0):
        run_program(choice, my_critters)
        print()
        menu()
        choice = get_choice()
        print()
    print("Goodbye!")

def menu():
    print("--------------------")
    print("Main Menu:")
    print("1. Check on critters")
    print("2. Add new critter")
    print("3. Feed critter")
    print("4. Pet critter")
    print("5. Play with critter")
    print("6. Go to bed")
    print("0. Quit")
    print()

def get_choice():
    """
    Purpose: Gets valid option number from user.
    Parameter: None.
    Return: userChoice (type: int)
    """
    valid = ["0", "1", "2", "3", "4", "5", "6"]
    user_choice = input("Choice? ")

    while user_choice not in valid:
        print()
        print("Invalid choice, try again.")
        print()
        menu()
        user_choice = input("Choice? ")

    return int(user_choice)

def run_program(choice, critters_list):
    if (choice == 1):
        check_critters(critters_list)

    elif (choice == 2):
        create_critter(critters_list)
    
    elif (choice == 3):
        feed_critter(critters_list)

    elif (choice == 4):
        pet_critter(critters_list)

    elif (choice == 5):
        play_critter(critters_list)

    else:
        sleep_critter(critters_list)

def sleep_critter(critters_list):
    if critters_list != []:
        critter = get_critter(critters_list)
        critters_list[critter-1].sleep()
    else:
        print("No critters here yet; try adding one!")

def play_critter(critters_list):
    if critters_list != []:
        critter = get_critter(critters_list)
        critters_list[critter-1].play()
    else:
        print("No critters here yet; try adding one!")

def pet_critter(critters_list):
    if critters_list != []:
        critter = get_critter(critters_list)
        critters_list[critter-1].pet()
    else:
        print("No critters here yet; try adding one!")

def feed_critter(critters_list):
    if critters_list != []:
        critter = get_critter(critters_list)
        critters_list[critter-1].feed()
    else: 
        print("No critters here yet; try adding one!")
    
def get_critter(critters_list):
     valid = []

     print("Available critters:")
     for i in range(1, len(critters_list)+1):
        print("%d. %s" %(i, critters_list[i-1].get_name()))
        valid.append(i)

     critter = input("Please select a critter (number): ")
     while (critter.isalpha()) or int(critter) not in valid:
        print("That's not a valid choice. try again!")
        critter = input("Please select a critter: ")

     return int(critter)

def check_critters(critters_list):
    if (critters_list != []):
         print("The room has some critters in it:")
         for i in range(len(critters_list)):
            print()
            print(critters_list[i])
    else:
        print("No critters here yet; try adding one!")

def create_critter(critters_list):
    name = input("New critter's name: ")
    adj = input("What's an adjective that describes the critter? ")
    p1 = input("What's the critter's personal pronoun (e.g. she, they)? ")
    p2 = input("What's the critter's possessive pronoun (e.g. her, their)" +
                "? ")
    food = input("What does the critter like to eat? ") 

    critter = Critter(name, adj, p1, p2, food)
    critters_list.append(critter)

main()
