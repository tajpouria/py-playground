from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flaskblog.models import User


class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])

    confirm_password = PasswordField(
        'Confirm Password ', [EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('Username already taken! try another one.')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email already exist! try another one.')


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', [DataRequired()])

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Login')
