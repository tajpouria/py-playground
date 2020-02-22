import os
import secrets
from flask import url_for
from PIL import Image
from flaskblog import APP_ROOT, mail
from flask_mail import Message


def save_picture(profile_pic, output_size=(125, 125)):
    _, f_ext = os.path.splitext(profile_pic.filename)

    pic_fn = secrets.token_hex(16) + f_ext
    pic_path = os.path.join(APP_ROOT, 'static/profile_pics/users', pic_fn)

    i = Image.open(profile_pic)
    i.thumbnail(output_size)
    i.save(pic_path)

    return f'users/{pic_fn}'


def send_reset_password_email(user):
    message = Message('Flaskblog Reset Password Request',
                      sender=os.getenv('EMAIL_USER'), recipients=[user.email])
    jws = user.generate_jws()
    message.body = f'''<p><b>Resetting your password is easy. Just press the link below and follow the instructions. We'll have you up and running in no time.</b></p>
<a href="{url_for('reset_password', jws=jws , _external=True)}">Reset Password</a>
<p>If you did not make this request then simply ignore this email and no changes will be made.</p>
'''
    mail.send(message)
