from tkinter import *
import os

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        base_folder = os.path.dirname(__file__)
        true_path = os.path.join(base_folder, r"images\true.png")
        false_path = os.path.join(base_folder, r"images\false.png")

        self.score = Label(text="Score: ", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)

        self.question_box = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_box.create_text(
            150, 125,
            text="q text",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR
        )
        self.question_box.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file=true_path)
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file=false_path)
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()