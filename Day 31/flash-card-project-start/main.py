from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
cards = {}
# ------------------------- CREATE FLASHCARD---------------------------- #
try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/german_words.csv")
    cards = original_data.to_dict(orient="records")
else:
    cards = words_data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    current_card = random.choice(cards)
    window.after_cancel(flip_timer)
    german_word = current_card["German"]
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=german_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    english_word = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


def right_card():
    cards.remove(current_card)
    next_card()
    data = pandas.DataFrame(cards)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, width=50, height=50, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, width=50, height=50, command=right_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
