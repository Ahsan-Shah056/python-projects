with open("./Input/Names/invited_names.txt",'r') as f:
    names = f.readlines()

PLACEHOLDER = "[name]"
    
with open ("./Input/Letters/starting_letter.txt") as file:
    content = file.read()
    for name in names:
        str_name = name.strip()
        new_l = content.replace(PLACEHOLDER,str_name)
        with open (f"./Output/ReadyToSend/Letter_for_{str_name}",mode='w') as dt:
            dt.write(new_l)