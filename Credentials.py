#Credentials.py
#CMPT 120 Intro to Programmin
#Lab 5 - working wiht Strings and FUnctions
#Author: Jack Szumowski
#Created: 2019-02-25

def main():
    
    #get user's first and last names
    name = getName()
    
    #TODO modify this to generate a marist style username    
    uname = makeName(name)

    #ask user to create a new password
    #TODO modify this to ensure the password has at least8 characters
    passwd = checkPass()
    
    print("Account Configured. Your new email addres is", uname + "@marist.edu")
      

#functions

def getName():

    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    
    return [first,last]

getName()


def makeName(name):

    return name[0] + '.' + name[1]
    
makeName()


def checkPass():
    
    passwd = input("Create a new password: ")
    passLen = len(passwd)

    if(passLen >= 8):
        goodEnough = True
        
    else:
        goodEnough = False
    
        while goodEnough == False:
        
            print("Fool of a Took! That password is feeble")
            passwd = input("Create a new passsword: ")
            passLen2 = len(passwd)
            
            if(passLen2 >= 8):
                goodEnough = True

            else:
                goodEnough = False
        
        print("The force is strong in this one...")

        
checkPass()


main()




