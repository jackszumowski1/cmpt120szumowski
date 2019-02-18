#pi.py
#Description: Calculate the aproximation of pi by summing values then rounding to the n'th term
#Author: Jack Szumowski
#had to start commenting because it started getting confusing haha

import math

def main():

    print("We are going to calculate pi to the n'th term.")
    print("Let's hope we get close to pi, but we'll check that later")
    
    n = eval(input("What number would you like to go to: "))

    numer = 4.0
    denom = 1.0
    sign = 1

    #only 4 the first time
    piGuess = 4
    

    for i in range(n):

            
        piece1 = piGuess

        #recuring
        denom = denom + 2
        
        piece2 = numer / denom

        #used for my debug
        #print("p1 = ", piece1, ",", piece2)   
   
        #if its even subtract
        if(sign == 1):
            piGuess = piece1 - piece2

        #if its odd add
        if(sign == -1):
            piGuess = piece1 + piece2 

        

        #flip + to -
        sign = sign * -1

        
        
    print("Our guess at pi with what you inputed", n, "is", piGuess)
    pi = math.pi

    offBy = piGuess - pi
    print("Wow we were only off by", offBy)

main()
    
