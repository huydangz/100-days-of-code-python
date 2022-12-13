import random
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from forms import Search, Add, Update

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6dzzzWlSihBXox7C0sKR6b'
Bootstrap(app)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cafes')
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return render_template('cafes.html', cafes=cafes)

@app.route('/random')
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return render_template('cafes.html', cafes=[random_cafe])

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = Search()
    if form.validate_on_submit():
        location = form.location.data
        results = db.session.query(Cafe).filter(Cafe.location.contains(location))
        return render_template('search.html', form=form, cafes=results)
    return render_template('search.html', form=form)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = Add()
    if form.validate_on_submit():
        cafe = Cafe(
            name=form.name.data,
            map_url=form.map_url.data,
            img_url=form.img_url.data,
            location=form.location.data,
            has_sockets=(form.has_sockets.data == '✅'),
            has_toilet=(form.has_toilet.data == '✅'),
            has_wifi=(form.has_wifi.data == '✅'),
            can_take_calls=(form.can_take_calls.data == '✅'),
            seats=form.seats.data,
            coffee_price=form.coffee_price.data
        )
        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for('all_cafes'))
    return render_template('add.html', form=form)

@app.route('/update', methods=['GET', 'POST', 'PATCH'])
def update():
    cafe_id = request.args.get('id')
    cafe = Cafe.query.get(cafe_id)
    form = Update(
        name=cafe.name,
        map_url=cafe.map_url,
        img_url=cafe.img_url,
        location=cafe.location,
        has_sockets=('✅' if cafe.has_sockets else '❌'),
        has_toilet=('✅' if cafe.has_sockets else '❌'),
        has_wifi=('✅' if cafe.has_sockets else '❌'),
        can_take_calls=('✅' if cafe.has_sockets else '❌'),
        seats=cafe.seats,
        coffee_price=cafe.coffee_price
    )
    if form.validate_on_submit():
        cafe.name = form.name.data
        cafe.map_url = form.map_url.data
        cafe.img_url = form.img_url.data
        cafe.location = form.location.data
        cafe.has_sockets = (form.has_sockets.data == '✅')
        cafe.has_toilet = (form.has_toilet.data == '✅')
        cafe.has_wifi = (form.has_wifi.data == '✅')
        cafe.can_take_calls = (form.can_take_calls.data == '✅')
        cafe.seats = form.seats.data
        cafe.coffee_price = form.coffee_price.data
        db.session.commit()
        return redirect(url_for('all_cafes'))
    return render_template('update.html', form=form)

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    cafe_id = request.args.get('id')
    cafe = Cafe.query.get(cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('all_cafes'))

if __name__ == '__main__':
    app.run(debug=True)