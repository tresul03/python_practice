from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(element["text"], element["answer"]) for element in question_data]

brain = QuizBrain(question_bank)
while brain.quiz_is_running:
    brain.next_question()

print(f"You have completed the quiz. Your score was {brain.score}/{len(brain.question_list)}")