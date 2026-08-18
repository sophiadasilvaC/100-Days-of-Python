# from turtle import * - this imports everything, but it's better to import the specified thing from the module
# if its being used more than 3 times, if used once or twice import whole module
# from turtle import Turtle
import turtle as t

tim = t.Turtle()

# if not bundled with python standard libray then you need to install it
# the pacakge will get store in venv
import heroes
print(heroes.gen())



















screen = t.Screen()
screen.exitonclick()
