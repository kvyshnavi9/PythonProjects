class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.count = 0

    def still_has_questions(self):
        return  self.question_number < len(self.question_list)

    def next_method(self):
        question = self.question_list[self.question_number]
        self.question_number +=1
        user_input = input(f"Q.{self.question_number}: {question.text} : (True/False) ?")
        self.check_answer(user_input, question.answer)

    def check_answer(self, input, correct_answer):
        if input.lower() == correct_answer.lower():
            self.count+= 1
            print(f"You got it right!")
        else:
            print(f"That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.count}/{self.question_number}")
        print("\n")

    def final_result(self):
         print("You've completed the quiz")
         print(f"Your final score is {self.count}/{self.question_number}")