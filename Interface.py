#interface
from DrawCalc import *
from Graphics import *
from Buttons import *

def main():
    isClicked(calcWin, coords)

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

            #makes all the buttons clickable
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

                
                #Numbers
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
                    drawEqBox(calcWin)

                    spacer = 0
                    continue
                    
                #DEL
                elif px >= 140 and px <= 200 and py <= 385 and py >= 325:
                    
                    del eq[-1]
                    
                    #Equation Box
                    drawEqBox(calcWin)

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


                # add an item to memory
                elif px >= 10 and px <= 70 and py <= 385  and py >= 325:
                    mem = ans
                    #print(mem)

                # recall mem
                elif px >= 10 and px <= 70 and py <= 450 and py >= 390:
                    eq = []
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

                #clear mem
                elif px >= 205 and px <= 265 and py <= 450 and py >= 390:
                    mem = 0
                    #print(mem)

                # =
                if px >= 205 and px < 265 and py <= 385 and py > 325:


                    #draw a new box
                    drawEqBox(calcWin)

                    
                    eq = "".join(eq)
                    #figure it out
                    #print(eq)
                    yourEQ = listEQ(eq)
                    ans = math(yourEQ)                   
                    Text(Point(20 + spacer + 20, 35), ans).draw(calcWin)
                    
                px = 0
                py = 0
