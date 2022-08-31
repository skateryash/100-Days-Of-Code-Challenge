import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guess = []

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in correct_guess:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_guess.append(answer_state)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_data = data[data.state == answer_state]
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(answer_state)
