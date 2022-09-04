# def add(*args):
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
# print(add(3, 5, 15))

import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=600, height=400)

# Label
my_label = tkinter.Label(text="Yash Cube Classes", font=("Times Now ROman", 28, "bold"))
my_label.grid(column=1, row=1)

# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Button
def button_clicked():
    my_label["text"] = user_input.get()


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)


# New Button
new_button = tkinter.Button(text="Click New Button", command=button_clicked)
new_button.grid(column=3, row=1)

# Entry
user_input = tkinter.Entry(width=10)
user_input.grid(column=4, row=3)









window.mainloop()
