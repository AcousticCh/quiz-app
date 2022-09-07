from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterace:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # window creation
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR)
        # Label Creation
        self.score = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0, pady=20)

        # canvas creation
        self.question_window = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question_window.create_text(150, 125, text="placeholder", width=280)
        self.question_window.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        #Canvas Button Creation
        self.correct_img = PhotoImage(file="images/true.png")
        self.correct = Button(image=self.correct_img, command=self.check_true)
        self.incorrect_img = PhotoImage(file="images/false.png")
        self.incorrect = Button(image=self.incorrect_img, command=self.check_false)
        self.incorrect.grid(column=0, row=2, pady=20)
        self.correct.grid(column=1, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_window.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_window.itemconfig(self.question_text, text=q_text)
        else:
            self.correct.config(state="disabled")
            self.incorrect.config(state="disabled")
            self.question_window.itemconfig(self.question_text, text="You have reached the end of this quiz, congratulations")

    def check_true(self):
        user_answer = "True"
        is_right = self.quiz.check_answer(user_answer=user_answer)
        self.give_feedback(is_right=is_right)

    def check_false(self):
        user_answer = "False"
        is_right = self.quiz.check_answer(user_answer=user_answer)
        self.give_feedback(is_right=is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_window.config(bg="green")
        else:
            self.question_window.config(bg="red")

        self.window.after(1000, self.get_next_question)




