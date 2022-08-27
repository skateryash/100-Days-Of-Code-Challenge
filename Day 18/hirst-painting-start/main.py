# import colorgram
#
# rgb_color = []
# colors = colorgram.extract("image.jpg", 50)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
colormode(255)

my_turtle.penup()
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)


pos = my_turtle.position()
x = pos[0]
y = pos[1]

for _ in range(10):
    for _ in range(10):
        my_turtle.color(random.choice(color_list))
        my_turtle.dot(20)
        my_turtle.forward(50)
    y += 50
    my_turtle.goto(x, y)

screen = Screen()
screen.exitonclick()