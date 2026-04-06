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

def get_coordinate(x,y):
    print(x,y)


turtle.onscreenclick(get_coordinate)
turtle.mainloop()