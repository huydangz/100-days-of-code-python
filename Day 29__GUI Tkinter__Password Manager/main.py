# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import random
import pyperclip

letters = string.ascii_letters
symbols = string.punctuation
numbers = string.digits

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = []
    password += [random.choice(letters) for _ in range(nr_letters)]
    password += [random.choice(symbols) for _ in range(nr_symbols)]
    password += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password)
    result = "".join(password)
    en_Password.delete(0, END)
    en_Password.insert(0, string=result)

    pyperclip.copy(result)

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox

def save_password():
    web = en_Website.get()
    mail = en_Email.get()
    password = en_Password.get()

    if web == "" or mail == "" or password == "":
        messagebox.showinfo("Oops", "Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel("Confirm", f"These are the details entered:\nWebsite: {web}\nEmail: {mail}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as f:
                f.write(f"{web} | {mail} | {password}\n")
                en_Website.delete(0, END)
                en_Password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

tk = Tk()
tk.title("Password Manager")
tk.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

######## row 1 ########
lb_Website = Label(text="Website:")
lb_Website.grid(column=0, row=1)

en_Website = Entry(width=52)
en_Website.grid(column=1, row=1, columnspan=2, sticky='W')
en_Website.focus()

######## row 2 ########
lb_Email = Label(text="Email/Username:")
lb_Email.grid(column=0, row=2)

en_Email = Entry(width=52)
en_Email.grid(column=1, row=2, columnspan=2, sticky='W')
en_Email.insert(0, string="huy.dang@gmail.com")

######## row 3 ########
lb_Password = Label(text="Password:")
lb_Password.grid(column=0, row=3)

en_Password = Entry(width=33)
en_Password.grid(column=1, row=3, sticky='W')

bt_GenPass = Button(text="Generate Password", command=generate_password)
bt_GenPass.grid(column=2, row=3, sticky='W')

######## row 4 ########
bt_AddPass = Button(text="Add Password", width=44, command=save_password)
bt_AddPass.grid(column=1, row=4, columnspan=2, sticky='W')

tk.mainloop()