#Calculator.py
#Description: Write an on screen calculater that can do the 4 basic arithmetic functions
#Author: Jack Szumowski

#from Graphics import *

def main():


    #write the equation
    EQ = listEQ()

    math(EQ)
    
    """calcWin = GraphWin("Calculator", 340, 300)
    calcWin.setBackground("white")
    
    #convert box
    converterBox = Rectangle(Point(0,100), Point(340, 200))
    converterBox.setWidth(2)
    converterBox.setFill('cyan')
    converterBox.draw(calcWin)

    #Convert Button
    conButton = Rectangle(Point(120,138), Point(202, 162))
    conButton.setWidth(4)
    conButton.setFill('red')
    conButton.draw(calcWin)
    Text(Point(160,150), 'CONVERT').draw(calcWin)
    

    #Equation Box
    eqBox = Rectangle(Point(0,0), Point(340, 100))
    eqBox.setWidth(2)
    eqBox.setFill('peachpuff')
    eqBox.draw(calcWin)

    # type the equation in equation box
    myEQ = Text(Point(100, 90), yourEQ).draw(calcWin)

    #convert that into a list
    listEQ = list(yourEQ)
    listEQ = list(filter(str.strip, listEQ))
    Text(Point(100, 275), listEQ).draw(calcWin)
    

    
    #answer box
    ansBox = Rectangle(Point(0,200), Point(340, 300))
    ansBox.setFill('peachpuff')
    ansBox.setWidth(2)
    ansBox.draw(calcWin)
    
    #answer
    #ans = Text(Point(100, 275), myANS).draw(calcWin)
    """

#take an equation and put it in a list
def listEQ():

    eq = input("What is your equation:")
    
    return eq.split()


def math(yourEQ):

    hasProdDiv = True
    i = 1

    while len(yourEQ) > 1 and hasProdDiv:

        
        #multipy
        if yourEQ[i] == '*':
            print(yourEQ)
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
    print("The answer is", ans)


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
        

main()
