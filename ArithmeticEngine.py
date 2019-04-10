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
    
    while True:
        
        cmd = input("What computation do you want to perform: ")
        cmd = cmd.lower()
        
        while cmd != 'add' and cmd != 'sub' and cmd !='mult' and cmd != 'div' and cmd != 'quit':
            cmd = input("Sorry but " + cmd + " is not valid. Please re-enter a valid command: ")
            cmd = cmd.lower()
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            
        except ValueError:
            print("Enter only numbers!")
            continue
        
        if cmd == "add":
            
            result = a + b
            
        elif cmd == "sub":
            result = a - b
            
        elif cmd == "mult":
            result = a * b
            
        elif cmd == "div":
            div1 = int(input("Enter the first number: "))
            div2 = int(input("Enter the second number: "))
            
            try:
                frac = a / b # will crash if division by zero
            except:
                print("Unable to divide by zero!")
                continue
            
            result = a / b
            
        elif cmd == "quit":
            break
            
        
        print("The result is " + str(result) + ".\n")

def main():
    showIntro()
    doLoop()
    showOutro()

main()
