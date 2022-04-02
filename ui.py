import tkinter as tk
from quizlogic import QuizLogic

THEME_COLOR = "#375362"

class QuizzUi:

    def __init__(self, quizlogic: QuizLogic):
        self.quizlogic = quizlogic
        self.screen = tk.Tk()
        self.screen.title("Trivia🌏")
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text=f"score: {self.quizlogic.score}", font=("ariel", 15), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, fill="black", text="Question Here", font=("ariel", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        correctImage = tk.PhotoImage(file="./images/true.png")
        self.correct_button = tk.Button(border=0, highlightthickness=0, image=correctImage, command=self.clickTrueButton)
        wrongImage = tk.PhotoImage(file="./images/false.png")
        self.wrong_button = tk.Button(border=0, highlightthickness=0, image=wrongImage, command=self.clickFalseButton)
        self.correct_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.next_question()

        self.screen.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quizlogic.score}")
        if self.quizlogic.question_number < 10:
            question_txt = self.quizlogic.nextQuestion()
            self.canvas.itemconfig(self.question_text, text=question_txt)
        else:
            self.canvas.itemconfig(self.question_text, text="Game Over!")
            self.correct_button.config(state="disable")
            self.wrong_button.config(state="disable")

    def clickTrueButton(self):
        if self.quizlogic.checkAnswer() == "True":
            self.canvas.config(bg="green")
            self.quizlogic.score += 1
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000, self.next_question)

    def clickFalseButton(self):
        if self.quizlogic.checkAnswer() == "False":
            self.canvas.config(bg="green")
            self.quizlogic.score += 1
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000, self.next_question)