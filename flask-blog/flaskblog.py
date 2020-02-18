import os
from flask import Flask, render_template, url_for, redirect, flash
from forms import RegisterForm, LoginForm

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')

        redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'admin':
            flash('You\'ve been logged in!', 'success')

            return redirect(url_for('home'))
        else:
            flash(
                'Login unsuccessfull please check email and password and try again', 'danger')

    return render_template('login.html', title='Login', form=form)
