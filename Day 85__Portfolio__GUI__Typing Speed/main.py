import random
import threading
import time
from tkinter import *

FONT = ('Cambria', 20)
text = open("text.txt", "r").read().split("\n")
counter = 0
running = False

def inputKeyPress(event):
    global text, counter, running, lb_sample, en_input, lb_speed
    if not running:
        if not event.keycode in [16, 17, 18]:
            running = True
            t = threading.Thread(target=time_thread)
            t.start()
    if lb_sample.cget('text').startswith(en_input.get()):
        en_input.config(fg="blue")
    else:
        en_input.config(fg="red")
    if en_input.get() == lb_sample.cget('text')[:-1]:
        running = False
        en_input.config(fg="green")

def time_thread():
    global text, counter, running, lb_sample, en_input, lb_speed
    while running:
        time.sleep(0.1)
        counter += 0.1
        cps = len(en_input.get()) / counter
        cpm = cps * 60
        wps = len(en_input.get().split(" ")) / counter
        wpm = wps * 60
        lb_speed.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n{wps:.2f} WPS\n{wpm:.2f} WPM")

def reset():
    global text, counter, running, lb_sample, en_input, lb_speed
    running = False
    counter = 0
    lb_speed.config(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPM")
    lb_sample.config(text=random.choice(text))
    en_input.delete(0, END)

# ===================== GUI ==================================
tk = Tk()
tk.title("Typing speed tester")
tk.geometry("800x600")

lb_sample = Label(text=random.choice(text), font=FONT)
lb_sample.grid(row=0, column=0, columnspan=2)
lb_sample.place(relx=0.5, rely=0.1, anchor=CENTER)

en_input = Entry(width=40, font=FONT)
en_input.grid(row=1, column=0, columnspan=2)
en_input.place(relx=0.5, rely=0.2, anchor=CENTER)
en_input.bind("<KeyPress>", inputKeyPress)

lb_speed = Label(text="Speed: \n0.00 CPS\n0.00 CPM\n0.00 WPS\n0.00 WPS", font=FONT)
lb_speed.grid(row=2, column=0, columnspan=2)
lb_speed.place(relx=0.5, rely=0.4, anchor=CENTER)

bt_reset = Button(text="Reset", command=reset, font=FONT)
bt_reset.grid(row=3, column=0, columnspan=2)
bt_reset.place(relx=0.5, rely=0.6, anchor=CENTER)

tk.mainloop()
