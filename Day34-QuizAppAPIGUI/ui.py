from tkinter import *
from quiz_brain import QuizBrain
import os

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        base_folder = os.path.dirname(__file__)
        true_path = os.path.join(base_folder, r"images\true.png")
        false_path = os.path.join(base_folder, r"images\false.png")

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0, padx=20, pady=20)

        self.question_box = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.question_box.create_text(
            150,
            125,
            width=280,
            text="q text",
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR
        )
        self.question_box.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file=true_path)
        self.true_button = Button(
            image=true_image,
            highlightthickness=0, 
            command=self.check_ans_true
        )
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file=false_path)
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.check_ans_false
        )
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_box.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=q_text)
        else:
            self.question_box.itemconfig(self.question_text, text="You reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_ans_true(self):
        self.give_feedback(self.quiz.check_answer("true"))
        #self.get_next_question()

    def check_ans_false(self):
        self.give_feedback(self.quiz.check_answer("false"))
        #self.get_next_question()

    def give_feedback(self, is_correct:bool):
        if is_correct:
            self.question_box.config(bg="green")
        else:
            self.question_box.config(bg="red")
        self.window.after(1000, self.get_next_question)
