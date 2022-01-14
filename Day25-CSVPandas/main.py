from os import stat
import turtle
import pandas
import writer

scrn = turtle.Screen()
scrn.title("US States Game")
image = "blank_states_img.gif"
scrn.addshape(image)
turtle.shape(image)
scribe = writer.Writer()

states_info = pandas.read_csv("50_states.csv")
state_list = states_info["state"].to_list()

game_running = True
score = 0

while game_running:
    answer = scrn.textinput(title=f"{score}/50 States Guessed", prompt="Enter the name of a state:")
    if answer == None:
        game_running = False
        missed_states_dict = {"state": state_list}
        missed_states_df = pandas.DataFrame(data=missed_states_dict)
        missed_states_df.to_csv("missed_states.csv")
        break

    check_df = states_info.loc[states_info["state"].str.fullmatch(answer,case=False)]
    if len(check_df) > 0:
        score += 1
        state_list.remove(answer.title())
        scribe.write_state(name=check_df["state"].to_string(index=False), x=check_df["x"].max(), y=check_df["y"].max())

scrn.exitonclick()

#testing again
