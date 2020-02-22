from flask import render_template, redirect, flash, url_for, request, abort
from flask_login import current_user, login_user, login_required, logout_user
from flaskblog import app, db, bcrypt
from flaskblog.forms import (
    RegisterForm, LoginForm, UpdateProfileForm, NewPostForm, ResetPasswordRequestForm, ResetPasswordForm)
from flaskblog.models import User, Post
from flaskblog.helpers import save_picture, send_reset_password_email


@app.route("/")
@app.route("/home/<int:page_num>")
def home(page_num=1):
    posts = Post.query.order_by(Post.date_posted.desc())\
        .paginate(per_page=5, page=page_num)

    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                    password=bcrypt.generate_password_hash(form.password.data).decode('utf-8'))
        db.session.add(user)
        db.session.commit()

        flash(
            f'Account created for {form.username.data}! you can login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))

        flash(
            'Login unsuccessful please check email and password and try again', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateProfileForm()
    profile_pic = url_for(
        'static', filename=f'profile_pics/{current_user.image_file}')

    if form.validate_on_submit():
        if form.picture.data:
            profile_pic = save_picture(form.picture.data)
            current_user.image_file = profile_pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()

        flash('Your account has been successfully updated!', 'success')
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('account.html', title='Account', profile_pic=profile_pic, form=form)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = NewPostForm()

    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()

        flash(f'{form.title.data} successfully created!', 'success')
        return redirect(url_for('home'))

    return render_template('newPost.html', form=form, legend='New Post')


@app.route('/post/<int:post_id>', methods=['GET'])
@login_required
def specific_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404(
        description=f'There is no post with id {post_id}'
    )

    return render_template('specificPost.html', title="Post", post=post)


@app.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.filter_by(id=post_id).first_or_404(
        description=f'There is no post with id {post_id}'
    )

    form = NewPostForm()
    if form.validate_on_submit():
        if current_user.id != post.author.id:
            return abort(401)

        if not post.id:
            return abort(404)

        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('You Post successfully updated!', 'success')
        return redirect(url_for('specific_post', post_id=post_id))

    form.title.data = post.title
    form.content.data = post.content

    return render_template('newPost.html', title="Update Post", legend="Update Post", form=form)


@app.route('/post/<int:post_id>/delete')
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).filter_by(
        id=post_id
    ).first_or_404(description=f'There is no post with id {post_id}')

    if current_user.id != post.author.id:
        return abort(401)

    if not post.id:
        return abort(404)

    db.session.delete(post)
    db.session.commit()
    flash('Your post successfully deleted!', 'success')
    return redirect(url_for('home'))


@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()

        if not user:
            flash('There is no user with specifIed email!', 'warning')

        send_reset_password_email(user)
        flash(
            f'An email containing reset token sent to {form.email.data} !', 'info')
        return redirect(url_for('home'))

    return render_template('resetPasswordRequest.html', title='Reset Password', form=form)


@app.route('/reset-password/<jws>', methods=['GET', 'POST'])
def reset_password(jws):
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    user = User.verify_jws(jws)
    if not user:
        flash(f'Token is either invalid or expired', 'warning')
        return redirect(url_for('reset_password_request'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        user.password = bcrypt.generate_password_hash(form.password.data)
        flash('You password successfully updated!', 'success')
        return redirect(url_for('login'))

    return render_template('resetPassword.html', title='Reset Password', form=form)


@app.route("/user/posts/<int:user_id>/<int:page_num>")
def user_posts(user_id, page_num):
    user = User.query.filter_by(id=user_id).first_or_404()

    if not user:
        return user

    posts = Post.query.filter_by(user_id=user.id)\
        .order_by(Post.date_posted.desc())\
        .paginate(per_page=5, page=page_num)

    return render_template('userPosts.html', posts=posts, user=user)
