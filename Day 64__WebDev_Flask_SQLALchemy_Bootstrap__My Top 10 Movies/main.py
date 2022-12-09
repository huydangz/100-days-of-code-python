from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "d483988d79da3edbe3f267033f1edbb0"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    class Movie(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), unique=True, nullable=False)
        year = db.Column(db.Integer, nullable=False)
        description = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=True)
        ranking = db.Column(db.Integer, nullable=True)
        review = db.Column(db.String(250), nullable=True)
        img_url = db.Column(db.String(250), nullable=False)

    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField('Your rating out of 10 e.g 7.5', validators=[DataRequired()])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    # movies = db.session.query(Movie).all()
    # movies = Movie.query.all()
    movies = Movie.query.order_by(Movie.rating).all()
    count_down = len(movies)
    for movie in movies:
        movie.ranking = count_down
        count_down -= 1
    return render_template("index.html", movies=movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": API_KEY,
            "query": title,
        }
        data = requests.get(url=url, params=params).json()
        return render_template('select.html', results=data['results'])
    return render_template("add.html", form=form)

@app.route("/select")
def select():
    movie_id = request.args.get('id')
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
    }
    data = requests.get(url=url, params=params).json()
    movie = Movie(
        title=data['title'],
        year=data['release_date'].split('-')[0],
        description=data['overview'],
        rating=round(data['vote_average'], 1),
        ranking=data['vote_count'],
        review='',
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for('edit', id=movie.id))

if __name__ == '__main__':
    app.run(debug=True)
