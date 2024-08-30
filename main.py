from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(prompt="choose your colour: ", title="make your bet").lower()
colour_list = ["red", "green", "pink", "yellow", "blue", "purple"]
y_position = [-100, -50, 0, 50, 100, 150]
participant_list = []


for turtles in range(0, 6):
    participant_turtle = Turtle(shape="turtle")
    participant_turtle.penup()
    participant_turtle.color(colour_list[turtles])
    participant_turtle.goto(x=-230, y=y_position[turtles])
    participant_list.append(participant_turtle)

if user_bet:
    game = True
while game:
    for turtle in participant_list:
        if turtle.xcor() > 230:
            game = False
            if turtle.pencolor() == user_bet:
                print(f"you have won the bet. {user_bet} turtle won.")
            else:
                print(f"you have lost the bet. {turtle.pencolor()} turtle won.")


        turtle.forward(random.randint(1, 20))

screen.exitonclick()
