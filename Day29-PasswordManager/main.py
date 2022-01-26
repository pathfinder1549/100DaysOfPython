from tkinter import *
import os


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, "tomato.png")