import time
import random

# This is the print_pause helper function as in the instructions

def print_pause(my_string):
    print(my_string)
    time.sleep(2)

#I want the choices to be random in the intro

def play_game() :
    option1 = random.choice(["red box", "blue box", "basket of puppies", "golden box with no key",
                            "very old book", "Marauder's map", "tiny black box", "jar of something foul but glimmering"])
    option2 = random.choice(["old coffee can", "purple box with feathers", "invitation from a witch", "mysterious envelope",
                            "very old pirate's map", "box that says 'do not open'", "magical pumpkin", "a bag marked with skull and cross bones"])
    intro(option1, option2)
    

def intro(option1, option2):
    print_pause("You wake up one morning and find you had an unexpected and unseen visitor.")   
    print_pause("On your desk there are two mysterious things. \n One is a " + option1 + " and one is a " + option2 + ".")
    time.sleep(3)
    print("Things are about to get curiouser and curiouser!!!")
    open_it(option1, option2)
   

# def to decide what to open
def open_it(option1, option2):
    print_pause("It is not every day that a " + option1 + " or a " + option2 + " turn up in your house.")
    print_pause("Do you you dare to open a mysterious gift?")
    print_pause("Enter 1 to open the " + option1)
    print_pause("Enter 2 to open the " + option2)
    choice = ""
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == "1":
            foul_odor(option1)
        else:
           glimmering_treasures(option2)


def foul_odor(option1):
    print_pause("Oh the vile air!")
    print_pause("Touching the " + option1 + " unleashed an unimaginable stink! ")
    print_pause("The only thing that can save you now is to use your time turner and start again")
    print_pause("Enter 1 to grab your time turner and try again.")
    print_pause("Enter 2 to sucuumb to the foul stench.")
    choice = ""
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == "1":
            print("Time turner activated!")
            time.sleep(4)
            play_game()
        else:
            print("You have died and inglorious and stench-filled death. GAME OVER!")

def glimmering_treasures(option2):
    print_pause("What a glorious sight1")
    print_pause("Touching the " + option2 + " unleashed an avalanche of treasures! ")
    print_pause("You are very rich! But do you do dare try again for more wealth?")
    print_pause("Enter 1 to grab your time turner and try again.")
    print_pause("Enter 2 to live happily off your riches.")
    choice = ""
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
        if choice == "1":
            print("Time turner activated!")
            time.sleep(4)
            play_game()
        elif choice == "2":
            print("You have won enough for one day! GAME OVER!")
        else:
            "Hmmm, I don't understand"


# Run game on load
play_game()

