from tkinter import *
from tkinter import messagebox
from pandas import *
from random import choice
import os


### CONSTANTS ###
BACKGROUND_COLOR = "#B1DDC6"
FRONT_LANG = "French"
BACK_LANG = "English"


### INIT WORD DATA ###
base_folder = os.path.dirname(__file__)
user_data_path = os.path.join(base_folder, "data/words_to_learn.csv")
init_data_path = os.path.join(base_folder, "data/french_words.csv")
try:
    user_file_df = read_csv(user_data_path)
    word_list = user_file_df.to_dict(orient="records")
except FileNotFoundError:
    try:
        init_file_df = read_csv(init_data_path)
        word_list = init_file_df.to_dict(orient="records")
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="Error: Data file not found.")
current_word = {}


### GENERATE WORDS ###
def new_card():
    global flip_timer
    window.after_cancel(flip_timer)
    new_word()

def new_word():
    global flip_timer
    global current_word
    current_word = choice(word_list)
    card.itemconfig(card_image, image=card_front_img)
    card.itemconfig(title_text, text=FRONT_LANG, fill="black")
    card.itemconfig(word_text, text=current_word[FRONT_LANG], fill="black")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_word
    card.itemconfig(card_image, image=card_back_img)
    card.itemconfig(title_text, text=BACK_LANG, fill="white")
    card.itemconfig(word_text, text=current_word[BACK_LANG], fill="white")

def remove_word():
    global current_word
    global word_list
    if current_word in word_list:
        word_list.remove(current_word)
        learning_df = DataFrame(word_list)
        learning_df.to_csv(user_data_path, index=False)
    new_card()    


### UI SETUP ###
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# file path error workaround
right_image_path = os.path.join(base_folder, "images/right.png")
wrong_image_path = os.path.join(base_folder, "images/wrong.png")
front_image_path = os.path.join(base_folder, "images/card_front.png")
back_image_path = os.path.join(base_folder, "images/card_back.png")

# flash card area
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=front_image_path)
card_back_img = PhotoImage(file=back_image_path)
card_image = card.create_image(400, 263, image=card_front_img)
title_text = card.create_text(400, 150, text="title", fill="black", font=("Ariel", 40, "italic"))
word_text = card.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

# buttons
wrong_image = PhotoImage(file=wrong_image_path)
wrong_button = Button(image=wrong_image, command=new_card, highlightthickness=0, pady=50)
wrong_button.grid(column=0, row=1)
right_image = PhotoImage(file=right_image_path)
right_button = Button(image=right_image, command=remove_word, highlightthickness=0, pady=50)
right_button.grid(column=1, row=1)

new_word()
window.mainloop()