from tkinter import *
from tkinter import ttk
from math import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None # to be used globally in the functions


# TIMER RESET 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    title_l.config(text="Timer")
    mark_l.config(text="")
    
    global reps
    reps =0 # to restart the program

# TIMER MECHANISM 
def start():
    global reps 
    reps +=1
    work_sec = WORK_MIN *60
    short_sec = SHORT_BREAK_MIN *60
    long_sec =LONG_BREAK_MIN*60
    
    if reps % 8 == 0:
        title_l.config(text="Break" , fg=RED)
        countdown(long_sec)
        
    elif reps %2 ==0:
        title_l.config(text="Break" , fg=PINK)
        countdown(short_sec)
        
    else:
        title_l.config(text="Work" , fg=GREEN)
        countdown(work_sec)    
    
# COUNTDOWN MECHANISM 
 
def countdown(count):
    count_min = floor(count / 60)
    count_sec = count % 60 #Using remainders for seconds
    if count_sec < 10:
        count_sec = f"0{count_sec }" #Improved aesthetics
        
    canvas.itemconfig(timer_text , text=f"{count_min}:{count_sec}" )
    if count >0:
        global timer 
        timer = window.after(1000, countdown, count-1 )
    else:
        start()  
        mark = ""
        sessions = floor(reps/2)
        for i in range(sessions):
            mark += "✓"
            mark_l.config(text=mark)
               
   
# GUI SETUP 
window = Tk()
window.title("Pomodoro")
window.config(padx =100 , pady=50 , bg=YELLOW)



#Labels creations
title_l = Label(text="Timer" , fg=GREEN , font= (FONT_NAME , 50), bg=YELLOW)
title_l.grid(row=0,column=1)
mark_l = Label(fg=GREEN , font= (FONT_NAME , 40), bg=YELLOW)
mark_l.grid(column= 1 , row =3)


# canvas settings
canvas =Canvas(width=200 , height= 224 , bg = YELLOW , highlightthickness=0)
bg_image = PhotoImage(file="tomato.png") # you can change image from here
canvas.create_image(100 , 112, image = bg_image)
timer_text = canvas.create_text(103,130 , text= "00:00" , fill= "white" , font= (FONT_NAME , 35 , "bold")) 
canvas.grid(column=1 , row=1)



# button creations
style = ttk.Style()
style.configure("TButton", font=(FONT_NAME, 12))

start_b = ttk.Button(text="Start", command=start, style="TButton")
start_b.grid(column=0, row=2)
reset_b = ttk.Button(text="Reset", command=reset, style="TButton")
reset_b.grid(column=2, row=2)


window.mainloop()