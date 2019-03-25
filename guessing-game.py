"""
guessing-game.py
Author: Jack Szumowski
make a game where he user has to guess the animal that the computer is
"thinking of"""

def main():

    name = "cat"

    print("Let's see if you can guess the animal I am thinking of")
    print("To give up type quit")

    gotIt = True
    
    while gotIt == True:

        guess = input("What is your guess: ")

        #convert guess to lowercase
        guess = guess.lower()

        
        #check if they still want to play
        if guess == "quit":
            print("HAHA I have defeated you")
            gotIt = False

        else:   
            #check if it matches
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
















    
