from drawing import logo
import random
print (logo)

print("Welcome to the Number Guessing Game! \t")
print ("I'm thinking of a number between 1 and 100. \t")

choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(0,100)
if choice == "easy":
    tries =10
elif choice == "hard":
    tries =5    
def game(chance):
    for i in range (0,chance+1):
        
        if chance == 0:
            print ("You lose. ")
            print(f"The number was {number}")
            break
        if chance>0:
            print (f"You have {chance} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))
        elif guess ==number:
            print ("You won. Thanks for playing the game.")
            print(f"The number was {number}")
            break 
        if guess > number:
            print("Too high.")
        elif guess <number:
            print("Too low.")    
        chance -=1
           
        
        
        
        
game(tries)       