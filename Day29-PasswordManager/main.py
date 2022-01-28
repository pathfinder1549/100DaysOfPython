from email import message
from tkinter import *
from tkinter import messagebox
import os

#FONT = ("Ariel", 12, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    """Save field contents to data file"""
    
    # get contents of fields
    site = site_entry.get()
    user = user_entry.get()
    pw = pass_entry.get()
    
    # check for empty strings
    if site and user and pw:
        input_ok = messagebox.askokcancel(title=site, message=f"New entry:\nSite: {site}\nEmail: {user}\nPassword: {pw}\nIs this correct?")
    else:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
        input_ok = False

    # write to file
    if input_ok:
        with open("data.txt", mode="a") as file:
            file.write(f"{site} | {user} | {pw}\n")

        # reset fields
        site_entry.delete(0,END)
        user_entry.delete(0,END)
        user_entry.insert(0, "email.address@gmail.com")
        pass_entry.delete(0,END)
        site_entry.focus()

    
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
site_label.grid(column=0, row=1, sticky="e")

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky="e")

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3, sticky="e")

site_entry = Entry(width=36)
site_entry.grid(column=1, row=1, columnspan=2, sticky="ew", padx=5)
site_entry.focus()

user_entry = Entry(width=36)
user_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5)
user_entry.insert(0, "email.address@gmail.com")

pass_entry = Entry(width=27)
pass_entry.grid(column=1, row=3, sticky="ew", padx=5)

gen_button = Button(text="Generate Password", command=gen_password)
gen_button.grid(column=2, row=3, sticky="ew", padx=5)

add_button = Button(text="Add", command=add_entry, width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=5)

window.mainloop()