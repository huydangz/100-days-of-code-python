# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 8
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def bt_reset_clicked():
    global timer, reps
    tk.after_cancel(timer)
    reps = 0
    lb_Timer.config(text="Timer", fg="blue")
    canvas.itemconfig(canvas_text_id, text="00:00")
    lb_Ticker.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def bt_start_clicked():
    global reps
    reps += 1
    if reps % 8 == 0:
        countdown("{:02d}".format(LONG_BREAK_MIN), "00")
        lb_Timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        lb_Ticker.config(text="✓")
        countdown("{:02d}".format(SHORT_BREAK_MIN), "00")
        lb_Timer.config(text="Short Break", fg=PINK)
    else:
        lb_Ticker.config(text="")
        countdown("{:02d}".format(WORK_MIN), "00")
        lb_Timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(minute, second):
    canvas.itemconfig(canvas_text_id, text=f"{minute}:{second}")
    if minute == "00" and second == "00":
        bt_start_clicked()
    else:
        if second != "00":
            second = "{:02d}".format(int(second) - 1)
        else:
            minute = "{:02d}".format(int(minute) - 1)
            second = "59"
        global timer
        timer = tk.after(10, countdown, minute, second)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

tk = Tk()
tk.title("Pomodoro")
# tk.minsize(width=400, height=400)
tk.config(padx=70, pady=30, bg=YELLOW)
# tk.resizable(0, 0)

lb_Timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
lb_Timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas_text_id = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 20, "bold"), fill="white")
canvas.grid(column=1, row=1)

bt_start = Button(text="Start", width=10, command=bt_start_clicked, font=(FONT_NAME, 13, "bold"))
bt_start.grid(column=0, row=2)

bt_reset = Button(text="Reset", width=10, command=bt_reset_clicked, font=(FONT_NAME, 13, "bold"))
bt_reset.grid(column=2, row=2)

lb_Ticker = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
lb_Ticker.grid(column=1, row=3)

tk.mainloop()
