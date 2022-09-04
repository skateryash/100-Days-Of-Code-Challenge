import tkinter

window = tkinter.Tk()
window.title("Miles to KM Converter")
# window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# User Input Box
user_input = tkinter.Entry(width=10)
user_input.grid(column=1, row=0)

# Miles label
label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

# Is equal to label
label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)

# result label
label3 = tkinter.Label(text="0")
label3.grid(column=1, row=1)

# KM label
label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=1)


# Button
def miles_to_km():
    input_miles = int(user_input.get())
    result = round(input_miles * 1.6, 2)
    label3.config(text=result)


button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
