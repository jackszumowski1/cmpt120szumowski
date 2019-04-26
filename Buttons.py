#buttons.py

from Graphics import *

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

