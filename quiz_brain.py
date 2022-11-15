class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.quiz_is_running = True

    def next_question(self):
        for question in self.question_list:
            answer = str(input(f"Q.{self.question_number + 1}: {question.question_text}. (True/False)?: ")).lower()
            if answer.lower() == question.answer.lower():
                self.score += 1
                print(f"Correct. The answer was {answer}.")
            else:
                print(f"Incorrect. The answer was {question.answer.lower()}.")
            
            print(f"Your score is {self.score}/{len(self.question_list)}")
            
            self.question_number += 1
            
        self.quiz_is_running = False