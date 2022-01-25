from tkinter import *
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, "tomato.png")

top_label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg= GREEN, bg=YELLOW)
top_label.grid(column=1, row=0)

tomato = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
tomato.create_image(100, 112, image=tomato_img)
tomato.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
tomato.grid(column=1, row=1)

start_button = Button(text="Start", bg=PINK)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=PINK)
reset_button.grid(column=2, row=2)

check_marks = Label(text=CHECK, font=(FONT_NAME, 16, "normal"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()