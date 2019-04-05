# DrawCalc.py
# Draw Calculator window
# Author: Jack Szumowski

from Graphics import *
from Calculator import *

def drawCalc():

    calcWin = GraphWin("Calculator", 275, 400)
    calcWin.setBackground("teal")
    
    #Equation Box
    eqBox = Rectangle(Point(10,10), Point(265, 60))
    eqBox.setWidth(2)
    eqBox.setFill('darkturquoise')
    eqBox.draw(calcWin)

    #Create list that holds the coordinates of each button
    coords = []
    
    # FUNCTIONS

    # = Button
    eqButton = Rectangle(Point(205,330), Point(265, 390))
    eqButton.setWidth(1)
    eqButton.setFill('red')
    eqButton.draw(calcWin)
    Text(Point(235,360), '=').draw(calcWin)
    eqsize = (60,60)
    eqcords =[205,330]
    coords.append(eqcords)

    # del Button
    delButton = Rectangle(Point(200,330), Point(140, 390))
    delButton.setWidth(1)
    delButton.setFill('deepskyblue')
    delButton.draw(calcWin)
    Text(Point(170,360), 'DEL').draw(calcWin)
    delsize = (60,60)
    delcords =[200,140]
    coords.append(delcords)
    
    # - Button
    miButton = Rectangle(Point(205,265), Point(265,325))
    miButton.setWidth(1)
    miButton.setFill('deepskyblue')
    miButton.draw(calcWin)
    Text(Point(235,295), '-').draw(calcWin)
    misize = (60,60)
    micords =[205,265]
    coords.append(micords)
    
    # + Button
    plusButton = Rectangle(Point(205,260), Point(265,200))
    plusButton.setWidth(1)
    plusButton.setFill('deepskyblue')
    plusButton.draw(calcWin)
    Text(Point(235,230), '+').draw(calcWin)
    plussize = (60,60)
    pluscords =[205,260]
    coords.append(pluscords)

    # * Button
    multButton = Rectangle(Point(205,195), Point(265,135))
    multButton.setWidth(1)
    multButton.setFill('deepskyblue')
    multButton.draw(calcWin)
    Text(Point(235,165), 'X').draw(calcWin)
    multsize = (60,60)
    multcords =[205,195]
    coords.append(multcords)

    # / Button
    divButton = Rectangle(Point(205,130), Point(265,70))
    divButton.setWidth(1)
    divButton.setFill('deepskyblue')
    divButton.draw(calcWin)
    Text(Point(235,100), '/').draw(calcWin)
    divsize =(60,60)
    divcords =[205,130]
    coords.append(divcords)

    # NUMBERS
    
    # 9 Button
    nineButton = Rectangle(Point(200,130), Point(140,70))
    nineButton.setWidth(1)
    nineButton.setFill('powderblue')
    nineButton.draw(calcWin)
    Text(Point(170,100), '9').draw(calcWin)
    ninesize =(60,60)
    ninecords =[200,130]
    coords.append(ninecords)
    
    # 8 Button
    eightButton = Rectangle(Point(135,130), Point(75,70))
    eightButton.setWidth(1)
    eightButton.setFill('powderblue')
    eightButton.draw(calcWin)
    Text(Point(105,100), '8').draw(calcWin)
    eightsize = (60,60)
    eightcords =[135,130]
    coords.append(eightcords)
    
    # 7 Button
    sevButton = Rectangle(Point(70,130), Point(10, 70))
    sevButton.setWidth(1)
    sevButton.setFill('powderblue')
    sevButton.draw(calcWin)
    Text(Point(40,100), '7').draw(calcWin)
    sevsize = (60,60)
    sevcords =[70,130]
    coords.append(sevcords)
    
    # 6 Button
    sixButton = Rectangle(Point(200,195), Point(140,135))
    sixButton.setWidth(1)
    sixButton.setFill('powderblue')
    sixButton.draw(calcWin)
    Text(Point(170,165), '6').draw(calcWin)
    sixsize = (60,60)
    sixcords =[200,195]
    coords.append(sixcords)
    
    # 5 Button
    fiveButton = Rectangle(Point(135,195), Point(75,135))
    fiveButton.setWidth(1)
    fiveButton.setFill('powderblue')
    fiveButton.draw(calcWin)
    Text(Point(105,165), '5').draw(calcWin)
    fivesize = (60,60)
    fivecords =[135,195]
    coords.append(fivecords)
    
    # 4 Button
    fourButton = Rectangle(Point(70,195), Point(10, 135))
    fourButton.setWidth(1)
    fourButton.setFill('powderblue')
    fourButton.draw(calcWin)
    Text(Point(40,165), '4').draw(calcWin)
    foursize = (60,60)
    fourcords =[70,195]
    coords.append(fourcords)
    
    # 3 Button
    threeButton = Rectangle(Point(200,260), Point(140,200))
    threeButton.setWidth(1)
    threeButton.setFill('powderblue')
    threeButton.draw(calcWin)
    Text(Point(170,230), '3').draw(calcWin)
    threesize = (60,60)
    threecords =[200,260]
    coords.append(threecords)
    
    # 2 Button
    twoButton = Rectangle(Point(135,260), Point(75,200))
    twoButton.setWidth(1)
    twoButton.setFill('powderblue')
    twoButton.draw(calcWin)
    Text(Point(105,230), '2').draw(calcWin)
    twosize = (60,60)
    twocords =[135,260]
    coords.append(twocords)
    
    # 1 Button
    oneButton = Rectangle(Point(70,260), Point(10, 200))
    oneButton.setWidth(1)
    oneButton.setFill('powderblue')
    oneButton.draw(calcWin)
    Text(Point(40,230), '1').draw(calcWin)
    onesize = (60,60)
    onecords =[70,260]
    coords.append(onecords)
    
    # . Button
    decButton = Rectangle(Point(200,325), Point(140,265))
    decButton.setWidth(1)
    decButton.setFill('powderblue')
    decButton.draw(calcWin)
    Text(Point(170,295), '.').draw(calcWin)
    decsize = (60,60)
    deccords =[200,325]
    coords.append(deccords)
        
    # 0 button
    zButton = Rectangle(Point(135,325), Point(75,265))
    zButton.setWidth(1)
    zButton.setFill('powderblue')
    zButton.draw(calcWin)
    Text(Point(105,295), '0').draw(calcWin)
    zsize = (60,60)
    zcords =[135,325]
    coords.append(zcords)

    # C button
    cButton = Rectangle(Point(135,330), Point(75,390))
    cButton.setWidth(1)
    cButton.setFill('powderblue')
    cButton.draw(calcWin)
    Text(Point(105,360), 'C').draw(calcWin)
    zsize = (60,60)
    zcords =[135,330]
    coords.append(zcords)
    
    # negate Button
    negButton = Rectangle(Point(70,325), Point(10, 265))
    negButton.setWidth(1)
    negButton.setFill('deepskyblue')
    negButton.draw(calcWin)
    Text(Point(40,295), '+/-').draw(calcWin)
    negsize = (60,60)
    negcords =[70,325]
    coords.append(negcords)
    
    #sign name to bottom
    #just to fill some space :)
    Text(Point(37,380),'Jack Calc').draw(calcWin)

    #See where they clicked
    isClicked(calcWin, coords)
    
    
#called if it is clicked
  
def isClicked(calcWin, coords):

        #holds eqaution in list
        eq = []
        
        #spaces out numbers when printing
        spacer = 0
        
        while True:
            p = calcWin.getMouse()
            px = p.getX()
            py = p.getY()
            spacer += 10
            
            for i in coords:    
                
                # -
                if px >= 205 and px <= 265 and py <= 320 and py >=270:
                    
                    Text(Point(20 + spacer - 3,35), '-').draw(calcWin)
                    eq.append('|-|')
                    
                    
                # +
                elif px >= 205 and px <= 265 and py <= 265 and py >= 205:
                    
                    Text(Point(20 + spacer - 3,35), '+').draw(calcWin)
                    eq.append('|+|')
                    
                    
                # *
                elif px >= 205 and px <= 265 and py <= 200 and py >= 140:
                    
                    Text(Point(20 + spacer - 3, 35), '*').draw(calcWin)
                    eq.append('|*|')

                
                # /
                elif px >= 205 and px <= 265 and py <= 135 and py >= 75:
                    
                    Text(Point(20 + spacer - 3 ,35), '/').draw(calcWin)
                    eq.append('|/|')
                    

                # 9
                elif px >= 140 and px <= 200 and py <= 135 and py >= 75:
                    
                    Text(Point(20 + spacer - 5,35), '9').draw(calcWin)
                    eq.append("9")
                    
                
                # 6
                elif px >= 140 and px <= 200 and py <= 200 and py >= 140:
                    
                    Text(Point(20 + spacer - 5,35), '6').draw(calcWin)
                    eq.append("6")
                    

                # 3
                elif px >= 140 and px <= 200 and py <= 265 and py >= 205:
                    
                    Text(Point(20 + spacer - 5,35), '3').draw(calcWin)
                    eq.append("3")
                    
                
                #.
                elif px >= 140 and px <= 200 and py <= 320 and py >= 270:
                    
                    Text(Point(20 + spacer - 5,35), '.').draw(calcWin)
                    eq.append(".")
                    #continue"""

                # 8
                if px >= 75 and px <= 135 and py <= 135 and py >= 75:
                    
                    Text(Point(20 + spacer - 5,35), '8').draw(calcWin)
                    eq.append("8")
                    
                
                # 5
                elif px >= 75 and px <= 135 and py <= 200 and py >= 140:
                    
                    Text(Point(20 + spacer - 5,35), '5').draw(calcWin)
                    eq.append("5")
                    

                # 2
                elif px >= 75 and px <= 135 and py <= 265 and py >= 205:
                    
                    Text(Point(20 + spacer - 5,35), '2').draw(calcWin)
                    eq.append("2")
                    

                # 0
                elif px >= 75 and px <= 135 and py <= 320 and py >= 270:
                    
                    Text(Point(20 + spacer - 5,35), '0').draw(calcWin)
                    eq.append("0")
                    
                
                # 7
                elif px >= 10 and px <= 70 and py <= 135 and py >= 75:
                    
                    Text(Point(20 + spacer - 5 ,35), '7').draw(calcWin)
                    eq.append("7")
                    

                # 4
                elif px >= 10 and px <= 70 and py <= 200 and py >= 140:
                    
                    Text(Point(20 + spacer - 5,35), '4').draw(calcWin)
                    eq.append("4")
                    

                # 1
                elif px >= 10 and px <= 70 and py <= 265 and py >= 205:
                    
                    Text(Point(20 + spacer - 5,35), '1').draw(calcWin)
                    eq.append("1")
                    
                
                # +/-
                elif px >= 10 and px <= 70 and py <= 320 and py >= 270:
                    
                    Text(Point(20 + spacer - 7,35), '-').draw(calcWin)
                    eq.append('-')
                    

                # C
                if px >= 75 and px < 135 and py <= 385 and py > 325:

                    eq = []
                    
                    #Equation Box
                    eqBox = Rectangle(Point(10,10), Point(265, 60))
                    eqBox.setWidth(2)
                    eqBox.setFill('darkturquoise')
                    eqBox.draw(calcWin)

                    spacer = 0

                        
                    continue
                    
                
                    
                #DEL
                elif px >= 140 and px <= 200 and py <= 385 and py >= 325:
                    
                    del eq[-1]
                    
                    #Equation Box
                    eqBox = Rectangle(Point(10,10), Point(265, 60))
                    eqBox.setWidth(2)
                    eqBox.setFill('darkturquoise')
                    eqBox.draw(calcWin)

                    spacer = 10

                    #re-draw
                    
                    for i in eq:
                        spacer += 9
                        
                        if i == '|+|':
                            Text(Point(spacer + 10, 35), '+').draw(calcWin)
                            
                        elif i == '|-|':
                            Text(Point(spacer + 10, 35), '-').draw(calcWin)

                        elif i == '|*|':
                            Text(Point(spacer + 10, 35), '*').draw(calcWin)

                        elif i == '|/|':
                            Text(Point(spacer + 10, 35), '/').draw(calcWin)
                            
                        else:
                            Text(Point(spacer + 10, 35), i).draw(calcWin)
                        
                    
                    
                      
                # =
                if px >= 205 and px < 265 and py <= 385 and py > 325:


                    #draw a new box
                    eqBox = Rectangle(Point(10,10), Point(265, 60))
                    eqBox.setWidth(2)
                    eqBox.setFill('darkturquoise')
                    eqBox.draw(calcWin)

                    
                    eq = "".join(eq)
                    #figure it out
                    #print(eq)
                    yourEQ = listEQ(eq)
                    ans = math(yourEQ)                   
                    Text(Point(20 + spacer + 20, 35), ans).draw(calcWin)
                    
                    
                
                px = 0
                py = 0

drawCalc()




