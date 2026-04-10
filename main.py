import turtle 
import pandas
screen = turtle.Screen()
maps = turtle.Turtle()
screen.title("US StatesGame")
maps.penup()
maps.goto(0, 250)
maps.write("States", align="center", font=("Arial", 18, "bold"))
image = "states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv(r"states.csv")
guessed_state = []
score,count = 0,0
should_continue = True


while should_continue:
    answer_box = screen.textinput(title="guess the state", prompt="Whats the another state name")
    if answer_box is None:
        print("No answer entered")
    else:
        answer = answer_box.strip().lower()
        if answer == 'exit':
            should_continue = False
            maps.penup()
            maps.goto(354.0,281.0)
            maps.write(f"States found : {score}", align="right", font=("Arial", 10,))
        else:
            lower_states = data.state.str.lower()
            if count == 50:
                should_continue = False
                maps.write(f"Congratulations! Score {score} ", align="Center", font=("Calibri", 15,))
            else:
                if answer in lower_states.values:
                    if answer not in guessed_state:
                        guessed_state.append(answer)
                        city = data[lower_states == answer]
                        maps.goto(city.x.item(), city.y.item())
                        maps.write(city.state.item())
                        score = score + 1
                        count = count + 1
                        maps.penup()
                        maps.goto(-323.0, 301.0)
                        maps.hideturtle()
                        maps.write(f"States : {score}", align="right", font=("Calibri", 10,))
                    else:
                        maps.penup()
                        maps.goto(342.0, -276.0)  
                        maps.write(f"Guessed state is already guessed: current score {score}", align= "right", font= ("Calibri", 10))   
                else:
                    maps.penup()
                    maps.goto(-318.0, -283.0)
                    maps.write(f"States not found: current score {score}", align="left", font=("Calibri", 10, ))
#turtle.mainloop()
screen.exitonclick()