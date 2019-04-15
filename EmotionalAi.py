#EmotionalAi.py
# Author: Jack Szumowski
# Make an Ai that can change its emotions based on what you do to it
#Date: 4/14/19

import random

# Get the mode of interaction from the user
# Params: none
# Returns: an integer indicating one of reward, punish, joke, or threaten
def getInteraction(action):
    
    if action == 'r':
        return 1

    elif action == 'p':
        return 2

    elif action == 't':
        return 3

    elif action == 'j':
        return 4
    

# return a corresponding integer
# Based on a given emotion and action, determine the next emotional state
# Params:
# currEmotion -a current emotion
# userAction-a user interaction
# Returns: an emotion

def lookupEmotion(currEmotion, userAction):

    #if he is happy
    if currEmotion == 1:
        #and rewarded
        if userAction == 1:
            return 2

        #punished
        elif userAction == 2:
            return 3

        #threatened
        elif userAction == 3:
            return 5

        #joked
        elif userAction == 4:
            return 2

    # if he is very happy
    elif currEmotion == 2:
        #and rewarded
        if userAction == 1:
            return 2
        
        #punished
        elif userAction == 2:
            return 7
        
        #threatend
        elif userAction == 3:
            return 1
        
        #joked
        elif userAction == 4:
            return 2
        
    # if he is sad
    elif currEmotion == 3:
        #and rewarded
        if userAction == 1:
            return 1
        
        #punished
        elif userAction == 2:
            return 4
        
        #threatend
        elif userAction == 3:
            return 6
        
        #joked
        elif userAction == 4:
            return 9

    # if he is very sad
    elif currEmotion == 4:
        #and rewarded
        if userAction == 1:
            return 3
        
        #punished
        elif userAction == 2:
            return 5
        
        #threatend
        elif userAction == 3:
            return 6
        
        #joked
        elif userAction == 4:
            return 3
    
    # if he is scared
    elif currEmotion == 5:
        #and rewarded
        if userAction == 1:
            return 9
        
        #punished
        elif userAction == 2:
            return 7
        
        #threatend
        elif userAction == 3:
            return 6
        
        #joked
        elif userAction == 4:
            return 5

    # if he is very scared
    elif currEmotion == 6:
        #and rewarded
        if userAction == 1:
            return 5
        
        #punished
        elif userAction == 2:
            return 7
        
        #threatend
        elif userAction == 3:
            return 6
        
        #joked
        elif userAction == 4:
            return 5
        
    # if he is mad
    elif currEmotion == 7:
        #and rewarded
        if userAction == 1:
            return 9
        
        #punished
        elif userAction == 2:
            return 8
        
        #threatend
        elif userAction == 3:
            return 5
        
        #joked
        elif userAction == 4:
            return 8

    # if he is very mad
    elif currEmotion == 8:
        #and rewarded
        if userAction == 1:
            return 7
        
        #punished
        elif userAction == 2:
            return 10
        
        #threatend
        elif userAction == 3:
            return 6
        
        #joked
        elif userAction == 4:
            return 8
        
    # if he is nuetral
    elif currEmotion == 9:
        #and rewarded
        if userAction == 1:
            return 1
        
        #punished
        elif userAction == 2:
            return 3
        
        #threatend
        elif userAction == 3:
            return 5
        
        #joked
        elif userAction == 4:
            return 1

def opener():
    print("Roger is your new AI friend and you can do each of the following actions to him")
    print("Reward him(r), punish him(p), threaten him(t), or joke with him(j)")
    print("Each of these actions will change his emotional state. To stop talking with Roger type 'quit'")
    print("Roger will start as neutral")
    print("Have Fun!")
    

def response(num):

    #make a random number
    ans = random.randint(0,3)

    #list of responses for each emotion

    happList = ["Yay I am feeling pretty good right now","feelin good in this nieghborhood",":)","That was nice it makes me happy"]
    vhappList = ["I haven't felt this amazing in a longtime! XD", "WOOOOOOHOOOOO", "Today is the best day ever!", "You're so nice to me!!! XD"]
    sadList = ["Aw :(", "That makes me sad", "Don't be so mean :(", "No I feel bad"]
    vsadList = ["How can I be happy again after this", "Please stop it hurts :(((", "Can you please be nicer... please", "My robo heart can't take any more of this"]
    scareList = ["O no I am frightened", "That was scary", "Lets not do that again phew", ":0 wow that was scary"]
    vscareList = ["Oh my god no stop thats scaring me!", "OH GOD HELP ME", "AHHHHHHHHHHHH!!!!!", "Let's not do this anymore its very scary"]
    madList = ["HEY you better stop that!!", "You're making me upset", "You better stop that before I get pissed off", "Listen here buddy. Cut. That. Out."]
    neutralList = ["Ah back to normal", "Not bad. Not good. Just okay",":|", "back to my original state"]

    #return a random responce
    if num == 1:
        print("\nRoger:", happList[ans])
    
    
    elif num == 2:
        print("\nRoger:", vhappList[ans])

    elif num == 3:
        print("\nRoger:", sadList[ans])

    elif num == 4:
        print("\nRoger:", vsadList[ans])

    elif num == 5:
        print("\nRoger:", scareList[ans])

    elif num == 6:
        print("\nRoger:", vscareList[ans])
    
    elif num == 7:
        print("\nRoger:", madList[ans])

    elif num == 8:
        print("\nRoger:", neutralList[ans])


    
def main():

    opener()

    # reward = 1
    # punish = 2
    # threaten = 3
    #joke = 4

    """
    happy = 1
    very h = 2
    sad = 3
    v sad = 4
    scared = 5
    v scared = 6
    mad = 7
    v mad = 8
    nuetral = 9
    """

    
    emotion = 9

    # easier to use emotion
    emoNum = 9
    
    
    while 1 > 0:
            
        #get the action
        action = input("What would you like to do to Roger: ")

        action = action.lower()

        if action == 'quit':
            print("Thanks for playin \nYou left Roger feeling", emotion)
            break

        elif action == 'kill':
            print("How could you!? Roger is now dead...\nI hope it feels good to have killed the first feeling AI")
            break
        
        #catch typos  
        while action != 'r' and action != 'p' and action != 't' and action != 'j':                  
            action = input("Please enter a valid action: ")
            
        # convert it into a usable number
        reaction = getInteraction(action)
            
        # get the new emotion
        newEmotion = lookupEmotion(emoNum,reaction)

            
        if newEmotion == 1:
            emoNum = 1
            emotion = 'happy'
            response(1)

        elif newEmotion == 2:
            emoNum = 2
            emotion = 'estatic'
            response(2)

        elif newEmotion == 3:
            emoNum = 3
            emotion = 'sad'
            response(3)

        elif newEmotion == 4:
            emoNum = 4
            emotion = 'depressed'
            response(4)

        elif newEmotion == 5:
            emoNum = 5
            emotion = 'scared'
            response(5)

        elif newEmotion == 6:
            emoNum = 6
            emotion = 'terrified'
            response(6)

        elif newEmotion == 7:
            emoNum = 7
            emotion = 'angry'
            response(7)

        elif newEmotion == 8:
            emoNum = 8
            emotion = 'furious'
            print("Roger: If you do that again I might just sign myself off")

        
        #nuetral
        elif newEmotion == 9:
            emoNum = 9
            emotion = 'neutral'
            response(8)
            
        #leaving     
        elif newEmotion == 10:
            emonum = 10
            emotion = 'gone'
            print("\nRoger: You know what... I'm leaving")
            break
        
        print("Roger is", emotion, "right now")

        

        
        
            
            
            
main()
