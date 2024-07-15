import pandas as pd
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}



try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    orignal_data = pd.read_csv("data/french_words.csv")
    to_learn =orignal_data.to_dict(orient="records")
else:     
    to_learn =data.to_dict(orient="records")
 
 
#functions to be used later on
def flip_card():
    canvas.itemconfig(card_title,text = "English" , fill = "white")
    canvas.itemconfig(card_word,text = current_card["English"] , fill = "white")    
    canvas.itemconfig(card_background , image= card_back)

def new_card():
    global current_card , timer
    window.after_cancel(timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(card_title,text = "French", fill = "black")
    canvas.itemconfig(card_word,text = current_card["French"] , fill = "black")   
    canvas.itemconfig(card_background , image= card_front) 
    timer = window.after(3000 , flip_card)
    
    
def is_known():
    to_learn.remove(current_card)
    data_save=pd.DataFrame(to_learn)
    data_save.to_csv("data/words_to_learn.csv" , index=False )
    
    new_card()     
    
      
#UI

window =Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer = window.after(3000 ,flip_card)

#Canvas configuration
canvas =Canvas(width=800 , height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background =  canvas.create_image(400, 263, image = card_front)
card_title= canvas.create_text(400 , 150 ,text="" , font=("Ariel" , 40 ,"italic"),fill ="black")
card_word= canvas.create_text(400 , 263 ,text="" , font=("Ariel" , 60 ,"bold"),fill ="black")
canvas.config(bg = BACKGROUND_COLOR , highlightthickness=0 )
canvas.grid(column=0 , row=0, columnspan=2)


#Buttons
    
cross_image =PhotoImage(file="images/wrong.png")
unknown_button =Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR ,command= new_card)
unknown_button.grid(column=0,row=1)

right_image =PhotoImage(file="images/right.png")
correct_button =Button(image=right_image, highlightthickness=0 , bg=BACKGROUND_COLOR ,command= is_known)
correct_button.grid(column=1 ,row=1)



new_card()

window.mainloop()