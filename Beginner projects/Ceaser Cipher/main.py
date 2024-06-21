def ceaser(direct,plain_text,shift_amount):
    final_text = ""
    
    for letter in plain_text:
        if direction == "encode":
            if letter not in alphabet:
                final_text+=letter
            else:    
                position = alphabet.index(letter)            
                new_position = position + shift_amount
                final_text += alphabet[new_position]        
                
           
        elif direction == "decode":
            if letter not in alphabet:
                final_text+=letter
            else:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                final_text += alphabet[new_position]     
    print(f"The {direction}ed text is {final_text}")

from art import logo 
print (logo)


while True:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift>26:
        shift%=26
        
        
    ceaser(direct=direction,plain_text=text,shift_amount=shift) 
    
    choice =input("Do you want to restart the cypher? Type yes to restart or no to exit: \t")  
    
    if choice=="no":
        print("Goodbye")
        break
         