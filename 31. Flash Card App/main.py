from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
card_list = {}
selected_card = {}

# ---------------------------- CREATE A NEW FLASH CARD------------------------------ #
try:
    data = pd.read_csv("data/concepts_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/English to Malay.csv")
    card_list = original_data.to_dict(orient="records")
else:
    card_list = data.to_dict(orient="records")


def new_card():
    global selected_card, flip_timer
    window.after_cancel(flip_timer)
    selected_card = random.choice(card_list)
    canvas.itemconfig(card_question, text="English", fill="black")
    canvas.itemconfig(card_answer, text=selected_card["English"], fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_question, text="Malay", fill="white")
    canvas.itemconfig(card_answer, text=selected_card["Malay"], fill="white")


# ---------------------------- SAVE PROGRESS ------------------------------- #
def remove_card():
    card_list.remove(selected_card)
    print(len(card_list))
    df = pd.DataFrame(card_list)
    df.to_csv("data/concepts_to_learn.csv", index=False)
    new_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(407, 264, image=card_front_img)
card_question = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))
card_answer = canvas.create_text(400, 263, text="Malay", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

check_img = PhotoImage(file="./images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

cross_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

new_card()

window.mainloop()
