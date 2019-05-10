# interface
# Jack Szumowski
# Date: 05/09/2019
from Graphics import *
from Calculator import *


def isClicked(calcWin, coords):
    # holds equation in list
    eq = []

    # spaces out numbers when printing
    spacer = 0

    while True:
        p = calcWin.getMouse()
        px = p.getX()
        py = p.getY()
        spacer += 10

        # makes all the buttons clickable
        for i in coords:

            # -
            if px >= 205 and px <= 265 and py <= 320 and py >= 270:

                Text(Point(20 + spacer - 3, 35), '-').draw(calcWin)
                eq.append('|-|')


            # +
            elif px >= 205 and px <= 265 and py <= 265 and py >= 205:

                Text(Point(20 + spacer - 3, 35), '+').draw(calcWin)
                eq.append('|+|')

                # *
            elif px >= 205 and px <= 265 and py <= 200 and py >= 140:

                Text(Point(20 + spacer - 3, 35), '*').draw(calcWin)
                eq.append('|*|')

            # /
            elif px >= 205 and px <= 265 and py <= 135 and py >= 75:

                Text(Point(20 + spacer - 3, 35), '/').draw(calcWin)
                eq.append('|/|')


            # Numbers
            # 9
            elif px >= 140 and px <= 200 and py <= 135 and py >= 75:

                Text(Point(20 + spacer - 5, 35), '9').draw(calcWin)
                eq.append("9")

            # 6
            elif px >= 140 and px <= 200 and py <= 200 and py >= 140:

                Text(Point(20 + spacer - 5, 35), '6').draw(calcWin)
                eq.append("6")

            # 3
            elif px >= 140 and px <= 200 and py <= 265 and py >= 205:

                Text(Point(20 + spacer - 5, 35), '3').draw(calcWin)
                eq.append("3")

            # .
            elif px >= 140 and px <= 200 and py <= 320 and py >= 270:

                Text(Point(20 + spacer - 5, 35), '.').draw(calcWin)
                eq.append(".")

            # 8
            if px >= 75 and px <= 135 and py <= 135 and py >= 75:

                Text(Point(20 + spacer - 5, 35), '8').draw(calcWin)
                eq.append("8")

            # 5
            elif px >= 75 and px <= 135 and py <= 200 and py >= 140:

                Text(Point(20 + spacer - 5, 35), '5').draw(calcWin)
                eq.append("5")

            # 2
            elif px >= 75 and px <= 135 and py <= 265 and py >= 205:

                Text(Point(20 + spacer - 5, 35), '2').draw(calcWin)
                eq.append("2")

            # 0
            elif px >= 75 and px <= 135 and py <= 320 and py >= 270:

                Text(Point(20 + spacer - 5, 35), '0').draw(calcWin)
                eq.append("0")

            # 7
            elif px >= 10 and px <= 70 and py <= 135 and py >= 75:

                Text(Point(20 + spacer - 5, 35), '7').draw(calcWin)
                eq.append("7")

            # 4
            elif px >= 10 and px <= 70 and py <= 200 and py >= 140:

                Text(Point(20 + spacer - 5, 35), '4').draw(calcWin)
                eq.append("4")

            # 1
            elif px >= 10 and px <= 70 and py <= 265 and py >= 205:

                Text(Point(20 + spacer - 5, 35), '1').draw(calcWin)
                eq.append("1")

            # +/-
            elif px >= 10 and px <= 70 and py <= 320 and py >= 270:

                Text(Point(20 + spacer - 7, 35), '-').draw(calcWin)
                eq.append('-')

            # C
            if px >= 75 and px < 135 and py <= 385 and py > 325:
                eq = []

                # Equation Box
                drawEqBox(calcWin)

                spacer = 0
                continue

            # DEL
            elif px >= 140 and px <= 200 and py <= 385 and py >= 325:

                del eq[-1]

                # Equation Box
                drawEqBox(calcWin)

                spacer = 10

                # re-draw

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


            # add an item to memory
            elif px >= 10 and px <= 70 and py <= 385 and py >= 325:
                mem = ans
                # print(mem)

            # recall mem
            elif px >= 10 and px <= 70 and py <= 450 and py >= 390:
                mem = (str)(mem)
                eq.append(mem)
                Text(Point(20 + spacer + 7, 35), mem).draw(calcWin)
                spacer += 10

            # subract from mem
            elif px >= 75 and px <= 135 and py <= 450 and py >= 390:
                eq.append('|-|')
                Text(Point(20 + spacer + 7, 35), '-').draw(calcWin)
                spacer += 10

                mem = (str)(mem)
                eq.append(mem)
                Text(Point(20 + spacer + 17, 35), mem).draw(calcWin)
                spacer += 10

            # add to mem
            elif px >= 140 and px <= 200 and py <= 450 and py >= 390:
                eq.append('|+|')
                Text(Point(20 + spacer + 7, 35), '+').draw(calcWin)
                spacer += 10
                mem = (str)(mem)
                eq.append(mem)
                Text(Point(20 + spacer + 17, 35), mem).draw(calcWin)
                spacer += 10

            # clear mem
            elif px >= 205 and px <= 265 and py <= 450 and py >= 390:
                mem = 0
                # print(mem)

            # =
            if px >= 205 and px < 265 and py <= 385 and py > 325:
                # draw a new box
                drawEqBox(calcWin)

                eq = "".join(eq)
                # figure it out
                # print(eq)
                yourEQ = listEQ(eq)
                ans = math(yourEQ)
                Text(Point(20 + spacer + 20, 35), ans).draw(calcWin)

            px = 0
            py = 0

def drawEqBox(calcWin):
    eqBox = Rectangle(Point(10, 10), Point(265, 60))
    eqBox.setWidth(2)
    eqBox.setFill('darkturquoise')
    eqBox.draw(calcWin)

def makeButtons(calcWin):
        # make buttons
        # = Button
        Buttons = [Button(205, 390, 265, 330, 235, 360, '=', 'red', calcWin),

                   # del Button
                   Button(140, 390, 200, 330, 170, 360, 'DEL', 'powderblue', calcWin),

                   # - Button
                   Button(205, 265, 265, 325, 235,  295, '-', 'powderblue', calcWin),

                   # + Button
                   Button(205, 260, 265, 200, 235, 230, '+', 'powderblue', calcWin),

                   # * Button
                   Button(205, 195, 265, 135, 235, 165,  'X', 'powderblue', calcWin),

                   # / Button
                   Button(205, 130, 265, 70, 235, 100, '/', 'powderblue', calcWin),

                   # NUMBERS
                   # 9 Button
                   Button(200, 130, 140, 70, 170, 100, '9', 'deepskyblue', calcWin),

                   # 8 Button
                   Button(135, 130, 75, 70, 105, 100,  '8', 'deepskyblue', calcWin),

                   # 7 Button
                   Button(70, 130, 10, 70, 40, 100,  '7', 'deepskyblue', calcWin),

                   # 6 Button
                   Button(200, 195, 140, 135, 170, 165, '6', 'deepskyblue', calcWin),

                   # 5 Button
                   Button(135, 195, 75, 135, 105, 165,  '5', 'deepskyblue', calcWin),

                   # 4 Button
                   Button(70, 195, 10, 135, 40,  165,  '4', 'deepskyblue', calcWin),

                   # 3 Button
                   Button(200, 260, 140, 200, 170, 230, '3', 'deepskyblue', calcWin),

                   # 2 Button
                   Button(135, 260, 75, 200, 105, 230, '2', 'deepskyblue', calcWin),

                   # 1 Button
                   Button(70, 260, 10, 200, 40, 230, '1', 'deepskyblue', calcWin),

                   # . Button
                   Button(200, 325, 140, 265, 170, 295, '.', 'deepskyblue', calcWin),

                   # 0 button
                   Button(135, 325, 75, 265, 105, 295, '0', 'deepskyblue', calcWin),

                   # C button
                   Button(135, 390, 75, 330, 105, 360, 'C', 'deepskyblue', calcWin),

                   # negate Button
                   Button(70, 325, 10, 265, 40, 295, '+/-', 'deepskyblue', calcWin),

                   # mem
                   Button(70, 390, 10, 330, 40, 360, 'M', 'deepskyblue', calcWin),

                   # memrec
                   Button(70, 455, 10, 395, 40, 425, 'MR', 'deepskyblue', calcWin),

                   # mem min
                   Button(75, 455, 135, 395, 105, 425, 'M-', 'deepskyblue', calcWin),

                   # mem plus
                   Button(140, 455, 200, 395, 170, 425, 'M+', 'deepskyblue', calcWin),

                   # mem clear
                   Button(205, 455, 265, 395, 235, 425, 'MC', 'deepskyblue', calcWin)]

        coords = []
        eqcords = [205, 330]
        coords.append(eqcords)

        delcords = [200, 140]
        coords.append(delcords)

        micords = [205, 265]
        coords.append(micords)

        pluscords = [205, 260]
        coords.append(pluscords)

        multcords = [205, 195]
        coords.append(multcords)

        divcords = [205, 130]
        coords.append(divcords)

        ninecords = [200, 130]
        coords.append(ninecords)

        eightcords = [135, 130]
        coords.append(eightcords)

        sevcords = [70, 130]
        coords.append(sevcords)

        sixcords = [200, 195]
        coords.append(sixcords)

        fivecords = [135, 195]
        coords.append(fivecords)

        fourcords = [70, 195]
        coords.append(fourcords)

        threecords = [200, 260]
        coords.append(threecords)

        twocords = [135, 260]
        coords.append(twocords)

        onecords = [70, 260]
        coords.append(onecords)

        deccords = [200, 325]
        coords.append(deccords)

        zcords = [135, 325]
        coords.append(zcords)

        ccords = [135, 330]
        coords.append(ccords)

        negcords = [70, 325]
        coords.append(negcords)

        memcoords = [70, 390]
        coords.append(memcoords)

        memcoords = [70, 395]
        coords.append(memcoords)

        memcoords = [75, 395]
        coords.append(memcoords)

        memcoords = [140, 395]
        coords.append(memcoords)

        memcoords = [205, 395]
        coords.append(memcoords)

        #call it
        isClicked(calcWin, coords)

class Calc:

    def __init__(self):
        self.window = GraphWin("Calculator", 275, 460)
        self.window.setBackground("teal")

    def runCalc(self):
        drawEqBox(self.window)
        makeButtons(self.window)

class Button:

    def __init__(self, x1, y1, x2, y2, nx, ny, name, color, window):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.name = name
        self.color = color
        self.window = window
        self.nx = nx
        self.ny = ny
        self.setBasics()

    def setBasics(self):
        button = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
        button.setWidth(1)
        button.setFill(self.color)
        button.draw(self.window)
        Text(Point(self.nx, self.ny), self.name).draw(self.window)


def main():
    calc = Calc()
    calc.runCalc()

main()
