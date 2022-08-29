from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_forward():
    my_turtle.forward(10)


def move_backwards():
    my_turtle.backward(10)


def move_anti_clockwise():
    my_turtle.left(10)


def move_clockwise():
    my_turtle.right(10)


def clear_screen():
    my_turtle.clear()
    my_turtle.home()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_anti_clockwise)
screen.onkey(key="a", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()