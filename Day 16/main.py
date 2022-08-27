# import turtle

# from turtle import Turtle, Screen
#
# yash = Turtle()
# print(yash)
# yash.shape("turtle")
# yash.color("blue3")
# yash.fd(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pockemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)