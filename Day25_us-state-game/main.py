import turtle, csv, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read data from csv
data = pandas.read_csv("50_states.csv")
data_get = data.to_dict('records')
# print(data_get)
# print(data_get[0]['state'])
# print(len(data_get))


correct_guess_count = 0
guess_count = 1
answer_state = 'Default'
correct_guess_list = []
missing_state = []

while answer_state != None and guess_count < 50:
    answer_state = screen.textinput(title=f"{correct_guess_count}/50 States Correct",
                                    prompt="What's another State's name?").title()
    #print(answer_state, f"guess_count = {guess_count}")
    if answer_state == 'Exit':
        # save the missing states to a csv
        for state in data_get:
            if state not in correct_guess_list:
                missing_state.append(state)
        print(missing_state)
        data_missing_state = pandas.DataFrame(missing_state)
        data_missing_state.to_csv("missing_state.csv")
        break
    for state_data in data_get:
        if answer_state == state_data['state']:
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state.goto(state_data['x'],state_data['y'])
            state.write(f"{state_data['state']}")
            if answer_state not in correct_guess_list:
                correct_guess_list.append(answer_state)
                correct_guess_count += 1
    #print(correct_guess_list)
    guess_count += 1

#screen.exitonclick()
