#RoboStore
# Author: Jack Szumowski
# Description: make an interactive store with a few items
# Date: 04/29/19

class Product:

    #assign values
    def __init__(self, name, price, quantity):
    
        self.name = name
        self.price = price
        self.quantity = quantity


    #see if we have enough on hand
    def inStock(self, count):

        return self.quantity >= count


    #calculate cost
    def totCost(self, count):

        return count * self.price


    #decrease stock on hand
    def decStock(self, count):

        self.quantity -= count 

                               

products = [Product("Ultrasonic range finder", 2.50, 4),
            Product("Servo Motor", 14.99, 10),
            Product("Servo Controller", 44.95, 5),
            Product("Microcontroller Board", 34.95, 7),
            Product("Laser Range Finder", 149.99, 2),
            Product("Lithium Polymer Battery", 8.99, 8)]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    
    for i in range(0,len(products)):
        
        if products[i].inStock(1):
            
            print(str(i)+")",products[i].name, "$", products[i].price)
            print()

            
def main():
    
    cash = float(input("How much money do you have $"))
    
    while cash > 0:
        
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")

        if vals[0] == "done":
            print("Thanks for shopping with us!")
            break
        
        prodId = int(vals[0])
        count = int(len(vals))
            
        if products[prodId].inStock(count):
                
            if cash >= products[prodId].totCost(count):
                    
                products[prodId].decStock(count)
                cash -= products[prodId].totCost(count)
                    
                print("You purchased", count, products[prodId].name +".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
                    
            else:
                print("Sorry, you cannot afford that product.")

        else:
            print("Sorry, we are sold out of", products[prodId].name)
                

main()
