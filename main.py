import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. STATE GAME")

# firstly we have to show our picture when run so
image = "blank_states_img.gif"
screen.addshape(image)
# here we r adding a shape of image in turtle
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)


# now we have to check that user input is one of the in 50 states
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_state = []

while len(guess_state)<50:
    answer_state = screen.textinput(title=f"{len(guess_state)}/50 states correct",
                                    prompt="what's another state's name?").title()
    # title give first letter capital of a string

    if answer_state == Exit:
        break;

    if answer_state in all_states:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)




# screen.exitonclick()
# instead of this we can also use
turtle.mainloop()