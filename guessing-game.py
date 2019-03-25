"""
guessing-game.py
Author: Jack Szumowski
make a game where he user has to guess the animal that the computer is
"thinking of"""

def main():

    name = "cat"

    print("Let's see if you can guess the animal I am thinking of")

    gotIt = True
    
    while gotIt == True:

        guess = input("What is your guess: ")

        good = nameCheck(guess, name)

        if good == True:
            print("CONGRATS you got it right")
            gotIt = False

        else:
            print("Good try but no")
            gotIt = True


    
def nameCheck(guess, answer):

    if guess == answer:
        return True

    else:
        return False

main()
















    
