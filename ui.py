from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
TEXT_CONFIG = ("Arial", 16, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # using type hints quiz_brain: QuizBrain i.e. a class
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz-True/False")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.user_answer = True

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=TEXT_CONFIG)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_image, padx=20, pady=20, command=self.right_button)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_image, padx=20, pady=20, command=self.left_button)
        self.false_button.grid(column=1, row=2)

        self.score = Label(text="Score:0", bg=THEME_COLOR, fg="white", font=("Arial", 16, "bold"))
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def left_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question )
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")






