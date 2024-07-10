import pandas as pd
import turtle as tu

screen = tu.Screen()
screen.title("Us states Guessing game")
IMG = "blank_states_img.gif"
screen.addshape(IMG)
tu.shape(IMG)

# tu.mainloop()
data = pd.read_csv("50_states.csv")
all_state = data['state'].tolist()

guessed = []
while len(guessed) < 50 :
    answer = screen.textinput(title=f"{len(guessed)}/50 states guessed" , prompt= "Whats another states name?").title()

    if answer == "Exit":
        missed = []
        for state in all_state:
            if state not in guessed:
                missed.append(state)
        new_data = pd.DataFrame(missed)    
        new_data.to_csv("States_to_be_learned.csv")    
        break
    if answer in all_state:
        guessed.append(answer)
        t = tu.Turtle()
        t.hideturtle()
        t.penup()
        state_coor = data[data.state == answer]
        t.goto(state_coor.x.item() ,state_coor.y.item())
        t.write(state_coor.state.item())
        

