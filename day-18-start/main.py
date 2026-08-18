# from turtle import * - this imports everything, but it's better to import the specified thing from the module
# if its being used more than 3 times, if used once or twice import whole module
# from turtle import Turtle
import turtle as t

tim = t.Turtle()


for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



















screen = t.Screen()
screen.exitonclick()
