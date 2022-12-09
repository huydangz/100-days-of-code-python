from flask import Flask, render_template, request, url_for, redirect, send_from_directory, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# Line below only required once, when creating DB.
# with app.app_context():
#     db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        # Email already existed, direct to login page
        if User.query.filter_by(email=email).first():
            flash("Email already existed, please log in instead")
            return redirect(url_for('login'))
        else:
            password = request.form.get('password')
            hash_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
            name = request.form.get('name')
            user = User(email=email, password=hash_password, name=name)
            db.session.add(user)
            db.session.commit()

            # LOGIN USER
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email"),
        password = request.form.get("password")
        user = User.query.filter_by(email=email[0]).first()
        # Email does not exist
        if not user:
            flash("This email does not exist, please try again")
            return redirect(url_for('login'))
        else:
            #Password not correct
            if not check_password_hash(user.password, password):
                flash('Password not correct, please try again')
                return redirect(url_for('login'))
            else:
                # LOGIN USER
                login_user(user)
                return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
