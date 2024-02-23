deck=['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'BS', 'BT', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'RS', 'RT', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'YS', 'YT', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'GS', 'GT']
pile=['holder']

top=pile[-1]

from random import randint



def draw(n,hand):
    global deck
    global pile
    for rep in range(n): #repeats for number of draws
        global deck
        spot=len(deck)-1
        ca=deck[randint(0,spot)] # grabs card from deck
        hand.append(ca) # adds to hand
        deck.remove(ca) #removes from deck
        
        if len(deck)==0: #checks to see if deck is depleted
            global pile
            deck=pile # if so, makes deck pile
            deck.remove('holder')# removes holder
            pile=['holder'] #resets pile
            pile.append(deck[-1]) #puts card into pile
            deck.remove(pile[-1]) # removes card from deck
            top=pile[-1]
            print("deck has been reshuffled")
            






def uno_func():
    handp=[]
    handc=[]
    top=pile[-1]
    end=0 #establish sentinel
    draw(7,handp) #sets hands
    draw(7,handc)
    pile.append(deck[randint(0,len(deck))])#sets top/pile
    deck.remove(pile[-1]) #removes card from deck
    top=pile[-1]#reset top
    
    print("you play first")
    while end==0: # checks to see if game is done
        skip=0
        while skip==0:

            top=pile[-1]

            print("this is the top of the pile") #text showing hand and pile
            print(top)
            print("this is your hand")
            print(handp)
            print(handc)#delete later
            print("this is c hand")#delete later
            print("opponent has " + str(len(handc))+ " cards in hand")
            play=0
            valid=0
            for card in handp: # checks to see if anything is playable
                if card[0]==top[0] or card[1]==top[1]:
                    play=1

            if play==0:
                draw(1,handp)
                print("no avaliable play,draw a card")
                skip=1

            while play==1: #allows play
                choice=str(input("type in the card you would like to play!")) #lets you choose card
                for card in handp:
                    if card==choice: #make sure card choice is in hand
                        valid=1
                        
                if valid==1:
                    if choice[0]==top[0] or choice[1]==top[1]: #checks if its a good choice
                        pile.append(choice) #puts card in pile
                        handp.remove(choice) #removes card from set
                        top=pile[-1]#reset top
                        play=0
                        skip=1
                        
                        if choice[1]=="S": #skip function

                            print("opponent skips their turn")
                           
                            skip=0

                        if choice[1]=="T": #draw 2
                            skip=0
                            draw(2,handc)
                            print("opponent draws 2")

                    else:
                        print("invalid input")
                            
                            
                

                if valid==0:
                    print("invalid input,try again.")

            if len(handp)==0: #checks win condition
                end=1
                print("you win the game! congrats!")
                break
            
        if end==0:

            AI_rand(handc,handp) #runs AI
        

        if len(handc)==0: #checks win condition
            end=1
            print("you lose!")
            break

            

def AI_rand(hand1,hand2):
    skip=0 #sentinel
        
    while skip==0:
        print('rep')

        play=0 #sentinel
        top=pile[-1] # reset top
        

        
        for card in hand1: #checks to see if anything playable
        
            if card[0]==top[0] or card[1]==top[1]:
                play=1
                print (1)

       


            
        if play==0: #draws card
            draw(1,hand1)
            print(2)
            skip=1

  

        if play==1: 
            option=[]
            print(3)
            for card in hand1:
                print(4)
                if card[0]==top[0]or card[1]==top[1]: # puts cards in list
                    option.append(card)
                    print(5)
                    print(option)

            choice=randint(0,(len(option)-1))# randomly chooses card from list
            choose= option[choice]
            pile.append(choose) #adds to pile
            hand1.remove(pile[-1]) #removes from hand
            top=pile[-1]
            print(pile)
            print(top)
            print(6)
            skip=1

            if len(hand1)==0:
                end=1
                break

            if choose[1]=="S": #cpu takes another turn
                print("You skip your turn")
                skip=0

            if choose[1]=="T": #cpu takes another turn
                print("You draw 2 and skip")
                draw(2,hand2)
                skip=0
