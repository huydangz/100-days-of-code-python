# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    web = en_Website.get()

    if web == "":
        messagebox.showinfo("Oops", "Please don't leave website empty!")
    else:
        data = {}
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showinfo("Oops", "No data file found!")
        else:
            try:
                mail = data[web]["email"]
                password = data[web]["password"]
            except KeyError:
                messagebox.showinfo(f"{web}", f"Not found!\nYou can create new password for this website")
            else:
                messagebox.showinfo(f"{web}", f"Email: {mail}\nPassword: {password}")

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
import json

def save_password():
    web = en_Website.get()
    mail = en_Email.get()
    password = en_Password.get()

    if web == "" or mail == "" or password == "":
        messagebox.showinfo("Oops", "Please don't leave any field empty!")
    else:
        new_data = {
            web: {
                "email": mail,
                "password": password,
            }
        }
        data = {}
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
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

en_Website = Entry(width=33)
en_Website.grid(column=1, row=1, sticky='W')
en_Website.focus()

bt_Search = Button(text="Search", width=15, command=search)
bt_Search.grid(column=2, row=1, sticky='W')

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