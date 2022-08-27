from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()

# my_turtle.shape("turtle")
# my_turtle.color("blue")

# for _ in range(4):
#     my_turtle.right(90)
#     my_turtle.forward(100)

# for _ in range(20):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# for side in range(3,11):
#     angle = 360 / side
#     colormode(255)
#     my_turtle.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(side):
#         my_turtle.right(angle)
#         my_turtle.forward(100)

# my_turtle.pensize(10)
my_turtle.speed("fastest")
# angle = [0, 90, 180, 270]
#
#
# for _ in range(100):
#     colormode(255)
#     my_turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     my_turtle.setheading(random.choice(angle))
#     my_turtle.forward(30)
angle = 5

for _ in range(72):
    colormode(255)
    my_turtle.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    my_turtle.circle(100)
    my_turtle.left(angle)



screen = Screen()
screen.exitonclick()