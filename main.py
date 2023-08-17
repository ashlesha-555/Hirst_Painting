import random
import turtle as t

t.colormode(255)
timmy=t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
color=[(235, 228, 211), (217, 218, 223), (104, 106, 125), (213, 152, 91), (140, 140, 150), (186, 62, 32), (225, 212, 109), (199, 147, 173), (237, 215, 225), (105, 112, 170), (177, 159, 47), (218, 224, 219), (186, 19, 9), (38, 40, 21), (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132), (190, 187, 218), (230, 176, 172), (231, 65, 82)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
no_of_dots=100

for dot in range(1, no_of_dots+1):
    timmy.dot(20, random.choice(color))
    timmy.forward(50)
    if dot%10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen=t.Screen()
screen.exitonclick()