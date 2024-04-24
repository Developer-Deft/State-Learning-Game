import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


state_file = pandas.read_csv("50_states.csv")
all_states = state_file.state.to_list()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = (screen.textinput(title=f"{len(guessed_state)} / 50 States Correct",
                                     prompt="What's another state's name.").title())

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = state_file[state_file.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# screen.exitonclick()


