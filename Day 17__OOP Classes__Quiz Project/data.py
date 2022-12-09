import random


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def output(self):
        return f"{self.text}. (True/False)?: "

    def is_correct(self, choice):
        return self.answer.lower() == choice.lower()


class QuestionMachine:
    def __init__(self, question_bank):
        self.question_bank = []
        for item in question_bank:
            self.question_bank.append(Question(item["question"], item["correct_answer"]))
        self.score = 0
        self.current_question = 0

    def ask_question(self):
        random_question = random.choice(self.question_bank)
        self.current_question += 1
        choice = input(f"Q.{self.current_question}: {random_question.output()}")
        if random_question.is_correct(choice):
            print("You got it right!")
            self.score += 1
        else:
            print(f"That's wrong.")
        print(f"The correct aswer was: {random_question.answer}")
        print(f"Your current score is: {self.score}/{self.current_question}\n")
        self.question_bank.remove(random_question)


question_data = [
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Sports", "type": "boolean", "difficulty": "easy",
                                       "question": "Peyton Manning retired after winning Super Bowl XLIX.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Tennis was once known as Racquetball.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "The Olympics tennis court is a giant green screen.", "correct_answer": "True",
     "incorrect_answers": ["False"]}, {"category": "Sports", "type": "boolean", "difficulty": "easy",
                                       "question": "Roger Federer is a famous soccer player.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "Formula E is an auto racing series that uses hybrid electric race cars.", "correct_answer": "False",
     "incorrect_answers": ["True"]}, {"category": "Sports", "type": "boolean", "difficulty": "easy",
                                      "question": "In Rugby League, performing a &quot;40-20&quot; is punished by a free kick for the opposing team.",
                                      "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "In 2008, Usain Bolt set the world record for the 100 meters with one shoelace untied.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "medium",
     "question": "ATP tennis hosted several tournaments on carpet court before being replaced to reduce injuries.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Sports", "type": "boolean", "difficulty": "easy",
     "question": "There are a total of 20 races in Formula One 2016 season.", "correct_answer": "False",
     "incorrect_answers": ["True"]}
]
