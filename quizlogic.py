from data import questions, answers

class QuizLogic:
    def __init__(self):
        self.score = 0
        self.question_number = 0
        self.current_question = None

    def nextQuestion(self):
        self.current_question = questions[self.question_number]
        self.question_number += 1
        return f"Q {self.question_number}. {self.current_question}"
    
    def checkAnswer(self):
        indexNumber = questions.index(self.current_question)
        return answers[indexNumber]