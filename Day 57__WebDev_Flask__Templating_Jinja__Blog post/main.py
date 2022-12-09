import requests
from flask import Flask, render_template
from post import Post

rsp = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
data = rsp.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=data)

@app.route('/post/<int:blog_id>')
def get_post(blog_id):
    post = None
    for item in data:
        if item["id"] == blog_id:
            post = Post(id=item["id"], title=item["title"], subtitle=item["subtitle"], body=item["body"])
            break
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
