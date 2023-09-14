'''
import turtle
from turtle import Turtle, Screen

screen = Screen()
img = 'asia.gif'
screen.addshape(img)
turtle.shape(img)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
'''
# import asian_coordinates

import turtle
from turtle import Turtle, Screen
import pandas

data = pandas.read_csv("28_states.csv")

screen = Screen()
screen.title("India States Game")
screen.screensize(canvwidth=885, canvheight=1200)
screen.setup(width=1.0, height=1.0)

# screen.setup(width=889, height=1204)
# img = "india_states.gif"
img = "india_states_new.gif"
# screen.addshape(img)  # adding the shape to the screen
turtle.bgpic(img)

s = data["state"]
state_list = s.to_list()  # list of all the states
score = 0
total_score = 28

correct_guesses = []

turtle.penup()
while score < total_score:
    answer_state = screen.textinput(title=f"{score}/{total_score}", prompt="Type the name of the state.")
    # print(answer_state)

    # Converting the guess to Title case
    answer_state = answer_state.title()

    if answer_state == "Exit":
        states_left = {
            'States': []
        }
        for state in data.state:
            if state not in correct_guesses:
                states_left['States'].append(state)
        new_data = pandas.DataFrame(states_left)
        new_data.to_csv("states_to_learn.csv")
        break
    # Checking if the guess is among the 50  states
    if answer_state in state_list and answer_state not in correct_guesses:
        t = Turtle()
        t.hideturtle()
        t.penup()
        score += 1  # increasing the score
        correct_guesses.append(answer_state)  # appending the answer in the list

        ans_state = data[data["state"] == answer_state]
        # Writing correct guesses onto the map
        t.goto(int(ans_state.x), int(ans_state.y))
        t.write(arg=answer_state, move=False)
        # turtle.goto(int(ans_state.x), int(ans_state.y))

screen.exitonclick()
