import html
import time
from tkinter import *
import requests

THEME_COLOR = "#375362"

score = 0
question_bank = []
question = {}

def load_question_bank():
    params = {
        "amount": 10,
        "type": "boolean",
        "category": 21
    }
    rsp = requests.get(url="https://opentdb.com/api.php", params=params)
    rsp.raise_for_status()
    data = rsp.json()
    global question_bank
    question_bank = data["results"]

def next_question():
    if question_bank:
        canvas.config(bg="white")
        canvas.update()
        global question
        question = question_bank[-1]
        canvas.itemconfig(cv_Text, text=html.unescape(question["question"]))
        question_bank.remove(question)
    else:
        canvas.config(bg="yellow")
        canvas.update()
        canvas.itemconfig(cv_Text, text="You've reached the end of questions.\nThank you.")
        bt_True.config(state="disabled")
        bt_False.config(state="disabled")

def update_score(chosen):
    if chosen == question["correct_answer"]:
        global score
        score += 1
        canvas.config(bg="green")
    else:
        canvas.config(bg="red")
    lb_Score.config(text=f"Score: {score}")
    canvas.update()
    time.sleep(0.7)

def bt_True_clicked():
    update_score("True")
    next_question()

def bt_False_clicked():
    update_score("False")
    next_question()

# ========================================================================
tk = Tk()
tk.title("Quizzler")
tk.config(padx=20, pady=20, bg=THEME_COLOR)

lb_Score = Label(text="Score: 0", font=("Ariel", 15, "bold"), fg="white", bg=THEME_COLOR)
lb_Score.grid(row=0, column=1)

canvas = Canvas(width=300, height=250, highlightthickness=0)
cv_Text = canvas.create_text(150, 125, width=280, text="Question here", font=("Ariel", 17, "italic"), fill=THEME_COLOR)
canvas.grid(row=1, column=0, columnspan=2, pady=20)

image_true = PhotoImage(file="images/true.png")
bt_True = Button(image=image_true, highlightthickness=0, command=bt_True_clicked)
bt_True.grid(row=2, column=0)

image_false = PhotoImage(file="images/false.png")
bt_False = Button(image=image_false, highlightthickness=0, command=bt_False_clicked)
bt_False.grid(row=2, column=1)

load_question_bank()
next_question()

tk.mainloop()
