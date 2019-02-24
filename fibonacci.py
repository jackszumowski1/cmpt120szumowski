#fibonacci.py
#Description: Write a program that will create a fibonacci sequence to the n'th number
#Author: Jack Szumowski

def main():

    print("We are going to calculate a fibonacci sequence to the n'th number")
    n = eval(input("What number would you like n to be: "))
        
    prior = 1
    former = 1

    if(n < 3):
        print("Your number is 1")

    else:
    
        for i in range(n-2):
    
            myNum = prior + former
            prior = former
            former = myNum

        print("Your number is", myNum)

    
main()
