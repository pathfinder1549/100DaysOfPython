from tkinter import *
import os


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, "logo.png")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=1)

window.mainloop()