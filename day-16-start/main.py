# import another_module
# print(another_module.another_variable)

from turtle import Turtle, Screen

# making a turtle object called timmy using the Turtle() class
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


