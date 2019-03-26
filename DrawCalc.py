# DrawCalc.py
# Draw Calculator window
# Author: Jack Szumowski

from Graphics import *
def drawCalc():

    calcWin = GraphWin("Calculator", 285, 400)
    calcWin.setBackground("teal")
    
    #Equation Box
    eqBox = Rectangle(Point(10,10), Point(275, 60))
    eqBox.setWidth(2)
    eqBox.setFill('darkturquoise')
    eqBox.draw(calcWin)


    # FUNCTIONS

    # = Button
    eqButton = Rectangle(Point(205,330), Point(275, 390))
    eqButton.setWidth(1)
    eqButton.setFill('red')
    eqButton.draw(calcWin)
    Text(Point(240,360), '=').draw(calcWin)

    # del Button
    eqButton = Rectangle(Point(200,330), Point(140, 390))
    eqButton.setWidth(1)
    eqButton.setFill('deepskyblue')
    eqButton.draw(calcWin)
    Text(Point(170,360), 'DEL').draw(calcWin)
        
    # - Button
    miButton = Rectangle(Point(205,265), Point(275,325))
    miButton.setWidth(1)
    miButton.setFill('deepskyblue')
    miButton.draw(calcWin)
    Text(Point(240,295), '-').draw(calcWin)
    
    # + Button
    plusButton = Rectangle(Point(205,260), Point(275,200))
    plusButton.setWidth(1)
    plusButton.setFill('deepskyblue')
    plusButton.draw(calcWin)
    Text(Point(240,230), '+').draw(calcWin)

    # * Button
    multButton = Rectangle(Point(205,195), Point(275,135))
    multButton.setWidth(1)
    multButton.setFill('deepskyblue')
    multButton.draw(calcWin)
    Text(Point(240,165), 'X').draw(calcWin)

    # / Button
    divButton = Rectangle(Point(205,130), Point(275,70))
    divButton.setWidth(1)
    divButton.setFill('deepskyblue')
    divButton.draw(calcWin)
    Text(Point(240,100), '/').draw(calcWin)


    # NUMBERS
    
    # 9 Button
    nineButton = Rectangle(Point(200,130), Point(140,70))
    nineButton.setWidth(1)
    nineButton.setFill('powderblue')
    nineButton.draw(calcWin)
    Text(Point(170,100), '9').draw(calcWin)
    
    # 8 Button
    eightButton = Rectangle(Point(135,130), Point(75,70))
    eightButton.setWidth(1)
    eightButton.setFill('powderblue')
    eightButton.draw(calcWin)
    Text(Point(105,100), '8').draw(calcWin)

    # 7 Button
    sevButton = Rectangle(Point(70,130), Point(10, 70))
    sevButton.setWidth(1)
    sevButton.setFill('powderblue')
    sevButton.draw(calcWin)
    Text(Point(40,100), '7').draw(calcWin)

    # 6 Button
    sixButton = Rectangle(Point(200,195), Point(140,135))
    sixButton.setWidth(1)
    sixButton.setFill('powderblue')
    sixButton.draw(calcWin)
    Text(Point(170,165), '6').draw(calcWin)
    
    # 5 Button
    fiveButton = Rectangle(Point(135,195), Point(75,135))
    fiveButton.setWidth(1)
    fiveButton.setFill('powderblue')
    fiveButton.draw(calcWin)
    Text(Point(105,165), '5').draw(calcWin)

    # 4 Button
    fourButton = Rectangle(Point(70,195), Point(10, 135))
    fourButton.setWidth(1)
    fourButton.setFill('powderblue')
    fourButton.draw(calcWin)
    Text(Point(40,165), '4').draw(calcWin)

    # 3 Button
    threeButton = Rectangle(Point(200,260), Point(140,200))
    threeButton.setWidth(1)
    threeButton.setFill('powderblue')
    threeButton.draw(calcWin)
    Text(Point(170,230), '3').draw(calcWin)
    
    # 2 Button
    twoButton = Rectangle(Point(135,260), Point(75,200))
    twoButton.setWidth(1)
    twoButton.setFill('powderblue')
    twoButton.draw(calcWin)
    Text(Point(105,230), '2').draw(calcWin)

    # 1 Button
    oneButton = Rectangle(Point(70,260), Point(10, 200))
    oneButton.setWidth(1)
    oneButton.setFill('powderblue')
    oneButton.draw(calcWin)
    Text(Point(40,230), '1').draw(calcWin)

    # . Button
    decButton = Rectangle(Point(200,325), Point(140,265))
    decButton.setWidth(1)
    decButton.setFill('powderblue')
    decButton.draw(calcWin)
    Text(Point(170,295), '.').draw(calcWin)
    
    # 0 button
    zButton = Rectangle(Point(135,325), Point(75,265))
    zButton.setWidth(1)
    zButton.setFill('powderblue')
    zButton.draw(calcWin)
    Text(Point(105,295), '0').draw(calcWin)

    # negate Button
    negButton = Rectangle(Point(70,325), Point(10, 265))
    negButton.setWidth(1)
    negButton.setFill('deepskyblue')
    negButton.draw(calcWin)
    Text(Point(40,295), '+/-').draw(calcWin)

    #sign name to bottom
    #just to fill some space :)
    a = Text(Point(68,380),'Jack Instruments').draw(calcWin)
    
    """# type the equation in equation box
    #myEQ = Text(Point(100, 90), yourEQ).draw(calcWin)

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

drawCalc()
"""
def drawIt(num):

    #when a number is clicked draw it in the box
    Text(Point

    
drawnum()


"""



