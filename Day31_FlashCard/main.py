from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"
BLACK_COLOR = "#000000"
current_card = {}


#--------------------------------- Step 2 - Create New Flash Cards ------------------------------------
# Use pandas to read csv
data = pandas.read_csv("./data/french_words.csv")
df = data.to_dict(orient="records")
# print(df)
# print out: [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'},

# def a function shows random word on flash card
def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # fix the bug about timer, 每翻一張卡就重新計算timer
    current_card = random.choice(df)
    canvas.itemconfig(canvas_image, image=ft_img)
    canvas.itemconfig(title_text, text=f"French", fill='black')
    canvas.itemconfig(word_text, text=f"{current_card['French']}", fill='black')
    flip_timer = window.after(3000, flip_card)

# ----------------------------------Step 3 Flip the card -------------------------------------

def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=bk_img)
    canvas.itemconfig(title_text, text=f"English", fill='white')
    canvas.itemconfig(word_text, text=f"{current_card['English']}", fill='white')


#--------------------------------- Step 1 - Create UI -------------------------------------------------
# create windows
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# create card front image
ft_img = PhotoImage(file="./images/card_front.png")
bk_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=ft_img)
canvas.grid(row=0, column=0, columnspan=2)

# # create texts on the canvas
title_text = canvas.create_text(400, 150, text="", fill=BLACK_COLOR, font=('Ariel', 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill=BLACK_COLOR, font=('Ariel', 60, "bold"))

# create buttons.
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=random_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=random_word)
wrong_button.grid(row=1, column=0)

random_word()


window.mainloop()
