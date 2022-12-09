import random
from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return '<h1 style="color:blue">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

rand_num = random.randint(0, 9)

@app.route('/<int:number>')
def guess_num(number):
    if number < rand_num:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif number > rand_num:
        return "<h1 style='color:purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif number == rand_num:
        return "<h1 style='color:green'>Yay. You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)