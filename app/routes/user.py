from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_login import login_user, logout_user

from ..functions import save_picture
from ..forms import LoginForm, RegistrationForm
from ..extensions import db, bcrypt
from ..models.user import User


user = Blueprint('user', __name__)

@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        avatar_filename = save_picture(form.avatar.data)
        user = User(name=form.name.data, login=form.login.data, avatar=avatar_filename, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"{form.name.data}, вы успешно зарегистрировались!", "success")
            return redirect(url_for('user.login'))
        except Exception as e:
            print(str(e))
            flash(f"При регистрации пользователя произошла ошибка!", "danger")
    return render_template('/user/register.html', form=form)


@user.route('/user/auth', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"{form.login.data}, вы успешно авторизовались!", "success")
            return redirect(next_page) if next_page else redirect(url_for('post.all'))
        else:
            flash(f"Ошибка входа. Пожалуйста проверьте логин и пароль!", "danger")
    return render_template('/user/login.html', form=form)


@user.route('/user/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('post.all'))