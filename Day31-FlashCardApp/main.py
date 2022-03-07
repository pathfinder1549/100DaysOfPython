from email.mime import image
from tkinter import *
import os

BACKGROUND_COLOR = "#B1DDC6"


### UI SETUP ###

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# file path error workaround
base_folder = os.path.dirname(__file__)
right_image_path = os.path.join(base_folder, "images/right.png")
wrong_image_path = os.path.join(base_folder, "images/wrong.png")
front_image_path = os.path.join(base_folder, "images/card_front.png")
back_image_path = os.path.join(base_folder, "images/card_back.png")

front_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file=front_image_path)
front_card.create_image(400, 263, image=front_img)
lang = front_card.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
word = front_card.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))
front_card.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file=right_image_path)
right_button = Button(image=right_image, highlightthickness=0, pady=50)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file=wrong_image_path)
wrong_button = Button(image=wrong_image, highlightthickness=0, pady=50)
wrong_button.grid(column=1, row=1)

window.mainloop()