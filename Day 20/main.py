from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x = 0.0
y = 0.0

for _ in range(3):
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    x -= 20
    snake.goto(x, y)






screen.exitonclick()
