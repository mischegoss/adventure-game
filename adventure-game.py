import time

# This is the print_pause helper function as in the instructions

def print_pause(my_string):
    print(my_string)
    time.sleep(2)

#I want the choices to be random in the intro

def play_game() :
    option1 = random.choice(["red box", "blue box", "basket of puppies", "golden box with no key",
                            "an old book", "a Marauder's map", "a tiny black box", "a jar of something foul but glimmering"])
    option2 = random.choice(["old key", "purple box with feathers", "an invitation", "a mysterious envelope",
                            "an old pirate's map", "a box that says 'do not open'", "a magical pumpkin", "a sorting hat"])


def intro():
    print_pause("You wake up one morning and find you had an unexpected visitor.")   
    print_pause("On your desk there are two mysterious things.  one is blue and one is red.")
    input("Press 1 to open the red package. Press 2 to to open the blue package")



intro(option1, option2)