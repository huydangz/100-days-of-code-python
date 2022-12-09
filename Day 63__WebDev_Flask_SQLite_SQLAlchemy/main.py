from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

with app.app_context():
    ##CREATE DATABASE
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
    # Optional: But it will silence the deprecation warning in the console.
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)


    ##CREATE TABLE
    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)

    db.create_all()


@app.route('/')
def home():
    ##READ ALL RECORDS
    return render_template('index.html', books=db.session.query(Book).all())


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # CREATE RECORD
        book = Book(
            title=request.form["book_name"],
            author=request.form["book_author"],
            rating=request.form["rating"]
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        #UPDATE RECORD
        book_id = request.form["id"]
        book = Book.query.get(book_id)
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    return render_template('edit.html', book=Book.query.get(book_id))

@app.route("/delete")
def delete():
    # DELETE A RECORD BY ID
    book_id = request.args.get('id')
    db.session.delete(Book.query.get(book_id))
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
