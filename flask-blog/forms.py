from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])

    confirm_password = PasswordField(
        'Confirm Password ', [EqualTo('password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
