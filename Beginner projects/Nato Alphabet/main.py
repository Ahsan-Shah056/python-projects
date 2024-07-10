import pandas as pd 
from drawing import *
data = pd.read_csv("nato_phonetic_alphabet.csv")
data = pd.DataFrame(data)

new_data = {row.letter:row.code for (index, row) in data.iterrows()}

print(logo)

user = input("Enter the word: ").upper()

final = [new_data[letter] for letter in user]
print (final)
