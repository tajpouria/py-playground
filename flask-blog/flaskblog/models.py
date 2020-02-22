import os
from itsdangerous import TimedSerializer
from datetime import datetime
from flask_login import UserMixin
from flaskblog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    image_file = db.Column(
        db.String(120), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"<User '{self.username}', '{self.email}', '{self.image_file}'>"

    def generate_jws(self):
        s = TimedSerializer(os.getenv('SECRET_KEY'), 'confirmation')
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_jws(jws, max_age_sec=1800):
        s = TimedSerializer(os.getenv('SECRET_KEY'), 'confirmation')

        try:
            user_id = s.loads(jws, max_age=max_age_sec)['user_id']
        except:
            return None

        return User.query.get(user_id)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"<Post '{self.title}', '{self.date_posted}'>"
