# DrawCalc.py
# Draw Calculator window
# Author: Jack Szumowski

from Graphics import *
from Calculator import *
from Buttons import *
from Interface import *

def setBasics(button, calcWin):
    button.setWidth(1)
    button.setFill('powderblue')
    button.draw(calcWin)

def setFunc(button, calcWin):
    button.setWidth(1)
    button.setFill('deepskyblue')
    button.draw(calcWin)

def drawEqBox(calcWin):
    eqBox = Rectangle(Point(10,10), Point(265, 60))
    eqBox.setWidth(2)
    eqBox.setFill('darkturquoise')
    eqBox.draw(calcWin)

"""def memRecall(m, want):

    if want == 'y':
        return mem

    else:
        mem = m"""

def drawCalc():

    calcWin = GraphWin("Calculator", 275, 460)
    calcWin.setBackground("teal")
    
    #Equation Box
    drawEqBox(calcWin)
    

    #Create list that holds the coordinates of each button
    coords = []
    
    # FUNCTIONS

    # = Button
    eqButton = Rectangle(Point(205,330), Point(265, 390))
    eqButton.setWidth(1)
    eqButton.setFill('red')
    eqButton.draw(calcWin)
    Text(Point(235,360), '=').draw(calcWin)
    eqcords =[205,330]
    coords.append(eqcords)

    # del Button
    delButton = Rectangle(Point(200,330), Point(140, 390))
    setFunc(delButton, calcWin)
    Text(Point(170,360), 'DEL').draw(calcWin)
    delcords =[200,140]
    coords.append(delcords)
    
    # - Button
    miButton = Rectangle(Point(205,265), Point(265,325))
    setFunc(miButton, calcWin)
    Text(Point(235,295), '-').draw(calcWin)
    micords =[205,265]
    coords.append(micords)
    
    # + Button
    plusButton = Rectangle(Point(205,260), Point(265,200))
    setFunc(plusButton, calcWin)
    Text(Point(235,230), '+').draw(calcWin)
    pluscords =[205,260]
    coords.append(pluscords)

    # * Button
    multButton = Rectangle(Point(205,195), Point(265,135))
    setFunc(multButton, calcWin)
    Text(Point(235,165), 'X').draw(calcWin)
    multcords =[205,195]
    coords.append(multcords)

    # / Button
    divButton = Rectangle(Point(205,130), Point(265,70))
    setFunc(divButton, calcWin)
    Text(Point(235,100), '/').draw(calcWin)
    divcords =[205,130]
    coords.append(divcords)

    # NUMBERS
    
    # 9 Button
    nineButton = Rectangle(Point(200,130), Point(140,70))
    setBasics(nineButton, calcWin)
    Text(Point(170,100), '9').draw(calcWin)
    ninecords =[200,130]
    coords.append(ninecords)
    
    # 8 Button
    eightButton = Rectangle(Point(135,130), Point(75,70))
    setBasics(eightButton, calcWin)
    Text(Point(105,100), '8').draw(calcWin)
    eightcords =[135,130]
    coords.append(eightcords)
    
    # 7 Button
    sevButton = Rectangle(Point(70,130), Point(10, 70))
    setBasics(sevButton, calcWin)
    Text(Point(40,100), '7').draw(calcWin)
    sevcords =[70,130]
    coords.append(sevcords)
    
    # 6 Button
    sixButton = Rectangle(Point(200,195), Point(140,135))
    setBasics(sixButton, calcWin)
    Text(Point(170,165), '6').draw(calcWin)
    sixcords =[200,195]
    coords.append(sixcords)
    
    # 5 Button
    fiveButton = Rectangle(Point(135,195), Point(75,135))
    setBasics(fiveButton, calcWin)
    Text(Point(105,165), '5').draw(calcWin)
    fivecords =[135,195]
    coords.append(fivecords)
    
    # 4 Button
    fourButton = Rectangle(Point(70,195), Point(10, 135))
    setBasics(fourButton, calcWin)
    Text(Point(40,165), '4').draw(calcWin)
    fourcords =[70,195]
    coords.append(fourcords)
    
    # 3 Button
    threeButton = Rectangle(Point(200,260), Point(140,200))
    setBasics(threeButton, calcWin)
    Text(Point(170,230), '3').draw(calcWin)
    threecords =[200,260]
    coords.append(threecords)
    
    # 2 Button
    twoButton = Rectangle(Point(135,260), Point(75,200))
    setBasics(twoButton, calcWin)
    Text(Point(105,230), '2').draw(calcWin)
    twocords =[135,260]
    coords.append(twocords)
    
    # 1 Button
    oneButton = Rectangle(Point(70,260), Point(10, 200))
    setBasics(oneButton, calcWin)
    Text(Point(40,230), '1').draw(calcWin)
    onecords =[70,260]
    coords.append(onecords)
    
    # . Button
    decButton = Rectangle(Point(200,325), Point(140,265))
    setBasics(decButton, calcWin)
    Text(Point(170,295), '.').draw(calcWin)
    deccords =[200,325]
    coords.append(deccords)
        
    # 0 button
    zButton = Rectangle(Point(135,325), Point(75,265))
    setBasics(zButton, calcWin)
    Text(Point(105,295), '0').draw(calcWin)
    zcords =[135,325]
    coords.append(zcords)

    # C button
    cButton = Rectangle(Point(135,330), Point(75,390))
    setBasics(cButton, calcWin)
    Text(Point(105,360), 'C').draw(calcWin)
    ccords =[135,330]
    coords.append(ccords)
    
    # negate Button
    negButton = Rectangle(Point(70,325), Point(10, 265))
    setFunc(negButton, calcWin)
    Text(Point(40,295), '+/-').draw(calcWin)
    negcords =[70,325]
    coords.append(negcords)

    memButton = Rectangle(Point(70,390), Point(10,330))
    setBasics(memButton,calcWin)
    Text(Point(40,360), "M").draw(calcWin)
    memcoords = [70,390]
    coords.append(memcoords)

    memRec = Rectangle(Point(70,395), Point(10,455))
    setBasics(memRec,calcWin)
    Text(Point(40,425), "MR").draw(calcWin)
    memcoords = [70,395]
    coords.append(memcoords)

    memMin = Rectangle(Point(75, 395), Point(135, 455))
    setBasics(memMin, calcWin)
    Text(Point(105, 425), "M-").draw(calcWin)
    memcoords = [75, 395]
    coords.append(memcoords)

    memPlus = Rectangle(Point(140, 395), Point(200, 455))
    setBasics(memPlus, calcWin)
    Text(Point(170, 425), "M+").draw(calcWin)
    memcoords = [140, 395]
    coords.append(memcoords)

    memClear = Rectangle(Point(205, 395), Point(265, 455))
    setBasics(memClear, calcWin)
    Text(Point(235, 425), "MC").draw(calcWin)
    memcoords = [205, 395]
    coords.append(memcoords)
    
    #sign name to bottom
    #just to fill some space :)
    #Text(Point(37,380),'Jack Calc').draw(calcWin)


    #See where they clicked
    #try:
    isClicked(calcWin, coords)
        
    #except 'AttributeError':
#called if it is clicked
  


drawCalc()




