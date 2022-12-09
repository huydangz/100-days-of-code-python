from flask import Flask

app = Flask(__name__)

@app.route('/')
def say_hello():
    return "Hello"


def make_bold(func):
    def deco_bold():
        return f'<b>{func()}</b>'
    return deco_bold


def make_emphasize(func):
    def deco_emphasize():
        return f"<em>{func()}</em>"
    return deco_emphasize

@app.route("/bye")
@make_bold
@make_emphasize
def say_bye():
    return "Bye"

@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are number {number}!"

@app.route("/qatar")
def wow():
    return "<h1 style='text-align: center'>Welcome to Qatar 2022</h1>" \
           "<p style='text-align: center'>This is calendar:</p>" \
           "<img src='https://i.etsystatic.com/35093217/r/il/d5f17e/4187269196/il_570xN.4187269196_fc8w.jpg' width=1000>"

if __name__ == "__main__":
    app.run(debug=True)




# =============================================================
# import time
# current_time = time.time()
# print(current_time)
#
# def speed_calc_decorator(function):
#     def decorated_function():
#         time1 = time.time()
#         function
#         time2 = time.time()
#         print(f'{function.__name__} run speed: {time2 - time1}')
#     return decorated_function
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(10000000):
#         i * i
# 
# @speed_calc_decorator
# def slow_function():
#     for i in range(100000000):
#         i * i
#
# fast_function()
# slow_function()

# =============================================================
# # Create the logging_decorator() function 👇
# def logging_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'You called {func.__name__}{args}')
#         print(f'It returned: {func(*args)}')
#     return wrapper
#
# # Use the decorator 👇
# @logging_decorator
# def a_function(*args):
#     return sum(args)
#
# a_function(1, 2, 3, 4)