from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create a list of question objects
question_bank = []
for question in question_data:
    new_question = Question(question["question"], question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.new_question()

print("Quiz Completed")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
