# from turtle import * - this imports everything, but it's better to import the specified thing from the module
# if its being used more than 3 times, if used once or twice import whole module
# from turtle import Turtle
import turtle as t
import random

tim = t.Turtle()

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)







# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()



















screen = t.Screen()
screen.exitonclick()
