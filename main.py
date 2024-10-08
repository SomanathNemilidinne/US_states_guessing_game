import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_states = pandas.read_csv("50_states.csv")
all_states = answer_states.state.to_list()
game_is_on = True
correct_guesses = []
while game_is_on:
    input_answer = screen.textinput(title=f"{len(correct_guesses)}/50 States are Correct", prompt="What's another state's name?")
    answer = input_answer.title()
    t = turtle.Turtle()
    if answer in all_states:
        correct_guesses.append(answer)
        t.hideturtle()
        t.penup()
        state_data = answer_states[answer_states.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer, False, "center", ('Arial', 5, 'normal'))
    if len(correct_guesses) == 50:
        game_is_on = False
        t.write("You did it! Congratulations", False, "right", ('Arial', 20, 'normal'))
    elif answer == "Exit":
        missed_states = []
        for state in all_states:
            if state not in correct_guesses:
                missed_states.append(state)
        missing_data = pandas.DataFrame(missed_states)
        missing_data.to_csv("States_Missed.csv")
        break
