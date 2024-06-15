import random
import words
import drawing


chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


logo = drawing.logo
print(logo)


# print(f'Pssst, the solution is {chosen_word}.')
from drawing import stages

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
        print(f"You've already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word:
        
        print(f"the letter {guess} is not a part of the word")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

   
    print(stages[lives])