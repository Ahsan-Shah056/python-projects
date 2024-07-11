from tkinter import *

window = Tk()
window.title("Miles to km ")
window.minsize(width=300 , height= 150)
window.config(padx= 15 , pady= 15)

label1 = Label(text="")
label1.grid(column=0,row=0)

label2 = Label(text="Miles")
label2.grid(column=2,row=0)

label3 = Label(text="is equal to")
label3.grid(column=0,row=1)

label4 = Label(text="KM")
label4.grid(column=3,row=1)

label5=Label()
label5.grid(column=1,row=1)


input =Entry()
input.config(width=7)
input.grid(column=1,row=0)
input.insert(END,string="0")


def find_val():
    value= float(input.get())
    km = value *1.609
    label5.config(text=km)
    
button= Button(text="Calculate", command= find_val)
button.grid(column=1 ,row=2)


window.mainloop()