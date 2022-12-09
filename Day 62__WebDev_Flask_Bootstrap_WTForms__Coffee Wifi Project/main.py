from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing time e.g. 7:30PM', validators=[DataRequired()])
    cafe_rating = SelectField("Coffee Rating", choices=['✘',  '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi_rating = SelectField("Wifi Strength Rating", choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    power_rating = SelectField("Power Socket Availability", choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['get', 'post'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        row = [form.cafe_name.data,
               form.cafe_location.data,
               form.opening_time.data,
               form.closing_time.data,
               form.cafe_rating.data,
               form.wifi_rating.data,
               form.power_rating.data]
        with open('cafe-data.csv', 'a', encoding='utf8', newline='\n') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding='utf8', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        rows = [row for row in csv_data]
    return render_template('cafes.html', cafes=rows)


if __name__ == '__main__':
    app.run(debug=True)
