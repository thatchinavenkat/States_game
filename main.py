import turtle 
import pandas

screen = turtle.Screen()
maps = turtle.Turtle()
screen.title("US Game")
maps.penup()
maps.goto(0, 250)
maps.write("States", align="center", font=("Arial", 18, "bold"))
image = "D://Python\CSV_excel\day-25-us-states-game-start\states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(r"D:\Python\CSV_excel\day-25-us-states-game-start\states.csv")
score = 0
should_continue = True
while should_continue:
    answer_box = screen.textinput(title="guess the state", prompt="Whats the another state name")
    if answer_box is None:
        print("No answer entered")
    else:
        answer = answer_box.strip().lower()
        if answer == 'exit':
            should_continue = False
            #print(f"Total Score : {score}")
            maps.write(f"States : {score}", align="right", font=("Arial", 18, "bold"))
        else:
            lower_states = data.state.str.lower()
            if answer in lower_states.values:
                city = data[lower_states == answer]
                x_axis = city.x.item()
                y_axis = city.y.item()
                maps.goto(x_axis, y_axis)
                maps.write(city.state.item())
                score = score + 1
                maps.penup()
                maps.goto(-323.0, 301.0)
                maps.write(f"States : {score}", align="right", font=("Arial", 10, "bold"))
            else:
                #print("State not found")
                maps.penup()
                maps.goto(-318.0, -283.0)
                maps.write(f"States not found: current score {score}", align="left", font=("Arial", 10, "bold"))
                #print(score)




#def get_coordinate(x,y):
#    print(x,y)


#turtle.onscreenclick(get_coordinate)
turtle.mainloop()
#screen.exitonclick()