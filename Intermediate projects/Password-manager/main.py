from tkinter import *
from tkinter import messagebox
from random import randint , choice , shuffle
import pyperclip  

# ---------------------------- SAVE Credentials ----------------------------
def add_info():
    """This funtion is used to store user's credential into a file"""
    if len(web_entry.get()) == 0 or len(email_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showinfo(title="RED Alert!!!!!" , message=" Don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get() , message=f"The entered details are \n Email: {email_entry.get()} \n Password: {pass_entry.get()} \n Are these correct?")
        
        if is_ok:
            with open("data.txt" , 'a') as file:
                file.write(f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()} \n")
            web_entry.delete(0, END)    
            pass_entry.delete(0, END) 
            email_entry.delete(0, END) 
        
         
# ---------------------------- Generating A PASSWORD  ------------------------------- #
def g_pass():
    pass_entry.delete(0 ,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(5, 10)
    nr_symbols = randint(2, 6)
    nr_numbers = randint(2, 6)

    password_list = []

 #---------------version 1 -------------------
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    
    
#---------------version 2 -------------------
    password_letter = [choice(letters) for i in range(nr_letters)]
    password_char = [choice(symbols) for i in range(nr_symbols)]
    password_numbers = [choice(numbers) for i in range(nr_numbers)]
   
    password_list = password_letter +password_char + password_numbers
    shuffle(password_list)

    password = ""
    password = "".join(password_list)
    
    pass_entry.insert(0 ,password)
    pyperclip.copy(password)
# ---------------------------- UI Configuration -------------------------------
window = Tk()
window.title("Passwrod Manager")
window.config(padx=40,pady=40)

canvas =Canvas(width=200 , height=200  ,highlightthickness=0)
bg_image = PhotoImage(file="logo.png")
canvas.create_image(100,100 , image=bg_image)
canvas.grid(column=1 , row=0)


# ---------------------------- Label ----------------------------
web_label = Label(text="Website:" ,font=("arial" , 14))
web_label.grid(column=0 , row=1)
name_label=Label(text="Username/Email: ",  font=("arial" , 14))
name_label.grid(column=0 , row=2)
password_label=Label(text="Password: ",  font=("arial" , 14))
password_label.grid(column=0 , row=3)

# ---------------------------- entries ----------------------------
web_entry = Entry( width = 35 )
web_entry.grid(column=1, row=1 , columnspan=2)
web_entry.focus( )

email_entry = Entry(width = 35)
email_entry.grid(column=1 , row=2 , columnspan=2)
pass_entry =  Entry(width= 21)
pass_entry.grid(column=1 , row=3 , columnspan=1)


    
# ---------------------------- buttons  ----------------------------
gen_pass = Button( text="Generate password", bg="black" , fg="black" ,command= g_pass)
gen_pass.grid(column=2 , row =3)
save_info = Button(text="Add information", bg="black" , fg="black" , command = add_info) 
save_info.grid(column=1 , row= 4, columnspan=2 )
window.mainloop()



