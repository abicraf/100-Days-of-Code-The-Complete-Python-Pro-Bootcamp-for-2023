from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quizbrian:QuizBrain):
        self.quiz = quizbrian

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score = 0", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Text Testing",
            font=('Arial', 24, 'italic'),
            fill='black'
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightbackground=THEME_COLOR, command=self.true_button)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightbackground=THEME_COLOR, command=self.false_button)
        self.false_button.grid(row=2, column=1)

        self.get_next_quiz_text()

        self.window.mainloop()

    def get_next_quiz_text(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score = {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_button(self):
        print("True button")
        # is_right=self.quiz.check_answer("True")
        self.get_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        print("False button")
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_quiz_text)

