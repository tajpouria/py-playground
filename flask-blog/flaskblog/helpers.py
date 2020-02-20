import os
import secrets
from PIL import Image
from flaskblog import APP_ROOT


def save_picture(profile_pic, output_size=(125, 125)):
    _, f_ext = os.path.splitext(profile_pic.filename)

    pic_fn = secrets.token_hex(16) + f_ext
    pic_path = os.path.join(APP_ROOT, 'static/profile_pics', pic_fn)

    i = Image.open(profile_pic)
    i.thumbnail(output_size)
    i.save(pic_path)

    return pic_fn
