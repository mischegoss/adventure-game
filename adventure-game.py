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
    option2 = random.choice(["old key", "purple box with feathers", "invitation from a witch", "mysterious envelope",
                            "very old pirate's map", "box that says 'do not open'", "magical pumpkin", "a sorting hat"])
    intro(option1, option2)
    

def intro(option1, option2):
    print_pause("You wake up one morning and find you had an unexpected and unseen visitor.")   
    print_pause("On your desk there are two mysterious things. \n One is a " + option1 + " and one is a " + option2 + ".")
    time.sleep(4)
    print("Things are about to get curiouser and curiouser!!!")
    open_it(option1, option2)


def open_it(option1, option2):
    print_pause("It is not every day that a " + option1 + option2 + "turn up in your house.")
    print_pause("Do you you dare to open a mysterious gift?")
    print_pause("Enter 1 to open the " + option1)
    print_pause("Enter 1 to open the " + option2)
    choice = ""
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")




play_game()


input("Press 1 to open the red package. Press 2 to to open the blue package")