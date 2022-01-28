from tkinter import *
import os

#FONT = ("Ariel", 12, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, "logo.png")

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

site_label = Label(text="Website:")
site_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

site_entry = Entry(width=35)
site_entry.grid(column=1, row=1, columnspan=2)

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", command=gen_password)
gen_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add_entry, width=36)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()