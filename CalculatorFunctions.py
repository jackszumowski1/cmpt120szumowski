#CalculatorFunctions.py
#Description: Write an on screen calculater that can do the 4 basic arithmetic functions
#Author: Jack Szumowski
"""
def figureItOut():
    
    #write the equation
    EQ = listEQ()

    math(EQ)

"""
#take an equation and put it in a list
def listEQ(eq):

    #eq = input("What is your equation:")

    eq = (str)(eq)
    eq = eq.split("|")      
    return eq              



def math(yourEQ):

    hasProdDiv = True
    i = 1

    while len(yourEQ) > 1 and hasProdDiv:

        
        #multipy
        if yourEQ[i] == '*':
            #print(yourEQ)
            p1 = float(yourEQ[i-1])
            p2 = float(yourEQ[i+1])

            #pass in p1 and p2 to multiply them
            mAns = mult(p1,p2)
            
            #remove the numbers used
            del yourEQ[i-1]
            del yourEQ[i-1]
            del yourEQ[i-1]
            
            #asign new number into the place of old numbers
            yourEQ.insert(i-1,mAns)
            i = 0
            #print(yourEQ)
            
        #Divide
        if yourEQ[i] == '/':
            p1 = float(yourEQ[i-1])
            p2 = float(yourEQ[i+1])
            dAns = div(p1,p2)

            #remove the numbers used
            del yourEQ[i-1]
            del yourEQ[i-1]
            del yourEQ[i-1]
            
            #asign new number into the place of old numbers
            yourEQ.insert(i-1,dAns)
            i = 0
        
        #None left?
        hasProdDiv = md(yourEQ)
        if hasProdDiv == False:
            i = 0
        i +=1
        
    #print(yourEQ)           

    #now lets add and subtract

    while len(yourEQ) > 1:
        
        #add
        if yourEQ[i] == "+":
            p1 = float(yourEQ[i-1])
            p2 = float(yourEQ[i+1])
            aAns = add(p1,p2)
            #remove the numbers used
            del yourEQ[i-1]
            del yourEQ[i-1]
            del yourEQ[i-1]
            
            #asign new number into the place of old numbers
            yourEQ.insert((i-1),aAns)
            
            i = 0
            
        #subtract
        if yourEQ[i] == "-":
            p1 = float(yourEQ[i-1])
            p2 = float(yourEQ[i+1])
            sAns = sub(p1,p2)
            #remove the numbers used
            
            del yourEQ[i-1]
            del yourEQ[i-1]
            del yourEQ[i-1]
            
            #asign new number into the place of old numbers
            yourEQ.insert(i-1,sAns)
            i = 0

        i += 1
    ans = yourEQ[0]
    #print("The answer is", ans)
    ans = round(ans, 4)
    
    return ans

def add(a,b):

        apart = a + b
        return apart
            
def sub(a,b):

        spart = a - b
        return spart    

def mult(a,b):

        mpart = a * b
        return mpart

def div(a,b):

        dpart = a / b
        return dpart


def md(yourEQ):

    for i in yourEQ:

        if(i == '*'):
            return True

        if(i == '/'):
            return True

    return False
        
