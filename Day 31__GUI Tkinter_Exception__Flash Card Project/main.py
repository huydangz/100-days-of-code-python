from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data = None
# ==============================================================================
import pandas
import random

try:
    data = pandas.read_csv("data/worlds_to_learn.csv")
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv("data/french_words.csv")
else:
    pass
finally:
    dict_data = data.to_dict(orient="records")

# ==============================================================================
def next_card():
    global current_card, timer
    tk.after_cancel(timer)
    current_card = random.choice(dict_data)
    cv.itemconfig(cv_text_title, text="French", fill="black")
    cv.itemconfig(cv_text_word, text=current_card["French"], fill="black")
    cv.itemconfig(cv_image, image=image_card_front)
    timer = tk.after(3000, flip_card)

def flip_card():
    cv.itemconfig(cv_text_title, text="English", fill="white")
    cv.itemconfig(cv_text_word, text=current_card["English"], fill="white")
    cv.itemconfig(cv_image, image=image_card_back)

def next_card_and_save():
    dict_data.remove(current_card)
    data = pandas.DataFrame(dict_data)
    data.to_csv("data/worlds_to_learn.csv", index=False)

    next_card()


# ==============================================================================
tk = Tk()
tk.title("Flash card")
tk.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
timer = tk.after(3000, flip_card)

cv = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_card_front = PhotoImage(file="./images/card_front.png")
image_card_back = PhotoImage(file="./images/card_back.png")
cv_image = cv.create_image(400, 263, image=image_card_front)
cv_text_title = cv.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
cv_text_word = cv.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
cv.grid(row=0, column=0, columnspan=2)

image_wrong = PhotoImage(file="./images/wrong.png")
bt_wrong = Button(width=100, height=99, image=image_wrong, highlightthickness=0, command=next_card)
bt_wrong.grid(row=1, column=0)

image_right = PhotoImage(file="./images/right.png")
bt_right = Button(width=100, height=99, image=image_right, highlightthickness=0, command=next_card_and_save)
bt_right.grid(row=1, column=1)

next_card()

tk.mainloop()
