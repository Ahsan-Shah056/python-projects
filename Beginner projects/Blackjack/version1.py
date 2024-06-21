from drawing import logo
import random

def blackjack():
    print (logo)
    play = True
    
    while play:
        game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if  game=='y':
                cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
                u1 = cards[random.randint(0,12)]
                u2 = cards[random.randint(0,12)]
                user_score=u1+u2
                print(f"Your hand is  {u1} and {u2} , Your score is: {user_score}.")
                

                c1 =cards[random.randint(0,12)]
            
                computer_score=c1
                print(f"computer's first card is {c1}, computer's score is: {computer_score}")
            
                
                if input("Press y if you want to draw another card or press n if you wish to end the game: ")=='y':
                    u3=cards[random.randint(0,12)]
                    user_score +=u3
                    print(f"Your final hand is {u1} , {u2} , {u3}, Your score is: {user_score}")
                
                
                c2 = cards[random.randint(0,13)]    
                computer_score+=c2
                if computer_score < 17:
                    c3 = cards[random.randint(0,13)]    
                    computer_score+=c3
                    print(f"computer's final hand is {c1},{c2},{c3} , computer's score is: {computer_score}")
                else:    
                    print(f"computer's final hand is {c1},{c2} , computer's score is: {computer_score}")
                
                
                if computer_score >21 :
                    print("The computer got busted. \nYou won the game") 
                elif user_score > 21 or user_score < computer_score:
                    print ("You lose. ")
                elif user_score > computer_score:
                    print("You got a higher score. \nYou won the game") 
                elif user_score == computer_score:
                    print("Its a draw. ") 
                    
        else:
            play=False 
            print("Thank you for playing.\nGoodbye")            
            
blackjack()                 