import requests
from flask import Flask, render_template

data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", data=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:id>')
def get_post(id):
    post = None
    for item in data:
        if item["id"] == id:
            post = item
            break
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)

