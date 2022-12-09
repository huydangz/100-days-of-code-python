import smtplib
from flask import Flask, render_template, request
import requests

MY_EMAIL = "lamasia30@gmail.com"
MY_PASSWORD = "zwtmosuqijrdvyam"
TO_EMAIL = "qhuy30@gmail.com"

posts = requests.get("https://api.npoint.io/d6b09ae60224f5d8ab09").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", message="Contact Me")
    else:
        with smtplib.SMTP("smtp.gmail.com", 587) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PASSWORD)
            conn.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f'subject:From Huy Dang Blog\n\n'
                    f'Name: {request.form["name"]}\n'
                    f'Email: {request.form["email"]}\n'
                    f'Phone: {request.form["phone"]}\n'
                    f'Message: {request.form["message"]}\n\n'
                    f'Regards.'
            )
        return render_template("contact.html", message="Successfully sent your message")

if __name__ == "__main__":
    app.run(debug=True)
