#Cmpt 120 - lab #6
# Jack Szumowski
# 4/1/19
###
def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult, 'sub, 'div' and 'quit'.\n")


def showOutro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come back again soon!")
    

def doLoop():

    a = True
    
    while a == True:
        
        cmd = input("What computation do you want to perform: ")
        cmd = cmd.lower()
        
        while cmd != 'add' and cmd != 'sub' and cmd !='mult' and cmd != 'div' and cmd != 'quit':
            cmd = input("Sorry but " + cmd + " is not valid. Please re-enter a valid command: ")
            cmd = cmd.lower()
        
        
        if cmd == "add":
            add1 = int(input("Enter the first number: "))
            add2 = int(input("Enter the second number: "))
            result = add1 + add2
            a = False
            
        elif cmd == "sub":
            sub1 = int(input("Enter the first number: "))
            sub2 = int(input("Enter the second number: "))
            result = sub1 - sub2
            a = False
            
        elif cmd == "mult":
            mult1 = int(input("Enter the first number: "))
            mult2 = int(input("Enter the second number: "))
            result = mult1 * mult2
            a = False
            
        elif cmd == "div":
            div1 = int(input("Enter the first number: "))
            div2 = int(input("Enter the second number: "))
            result = div1 / div2
            a = False
            
        elif cmd == "quit":
            break
        
    print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()