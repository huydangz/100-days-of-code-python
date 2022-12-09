from data import QuestionMachine, question_data

end_game = False
while not end_game:
    question_machine = QuestionMachine(question_data)
    while question_machine.question_bank:
        question_machine.ask_question()
    print(f"Your final score is: {question_machine.score}/{question_machine.current_question}\n")
    if input("Play again? 'y' or 'n") == 'n':
        end_game = True
