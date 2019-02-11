#rover.py
#Description: Calculate the time taken for a photo from mars to reach Earth
#Author: Jack Szumowski

def main():

    print("I am going to calculate the time it takes to send a photo from Mars to Earth")
    
    dist = 34000000
    speed = 186000

    time = dist / speed

    print("It took", time, "seconds to deliver the photo")

    

main()
