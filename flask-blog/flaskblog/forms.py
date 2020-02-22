from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flask_login import current_user
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


class UpdateProfileForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=2, max=20)])

    email = StringField('Email', [DataRequired(), Email()])

    picture = FileField('Profile Picture', [
                        FileAllowed(['jpg', 'png', 'jpeg'])])

    submit = SubmitField('Update')

    def validate_username(self, field):
        if field.data != current_user.username:
            user = User.query.filter_by(username=field.data).first()
            if user:
                raise ValidationError(
                    'Username is already taken! try another one.')

    def validate_email(self, field):
        if field.data != current_user.email:
            user = User.query.filter_by(email=field.data).first()
            if user:
                raise ValidationError(
                    'Email is already taken! try another one.'
                )


class NewPostForm(FlaskForm):
    title = StringField('Title', [DataRequired(), Length(min=2, max=125)])

    content = TextAreaField(
        'Content', [DataRequired(), Length(min=10, max=1000)])

    submit = SubmitField('Submit')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])

    submit = SubmitField('Send Reset Password Request')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()

        if not user:
            raise ValidationError(
                'There\'s no user with specified email address!')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', [DataRequired()])

    confirm_password = PasswordField(
        'Confirm Password ', [EqualTo('password')])

    submit = SubmitField('Sign Up')
