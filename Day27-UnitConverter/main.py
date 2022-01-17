from ast import Pass
from tkinter import *

# mi to km conversion
CONV_FACTOR = 1.60934

# define conversion
def convert():
    n1 = float(user_input.get())
    ans = n1 * CONV_FACTOR
    value.config(text=f"{ans:.2f}")

# create window
win = Tk()
win.title("Unit Converter")
win.minsize(width=100, height=100)
win.config(padx=20, pady=20)

# create objects and arrange window
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

unit_from = Label(text="mi")
unit_from.grid(column=2, row=0)

message = Label(text="is equal to ")
message.grid(column=0, row=1)

value = Label(text=" ")
value.grid(column=1, row=1)

unit_to = Label(text="km")
unit_to.grid(column=2, row=1)

btn = Button(text="Convert", command=convert)
btn.grid(column=1, row=2)

win.mainloop()