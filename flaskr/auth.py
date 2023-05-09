import functools

from flask import (
    Blueprint, g, request, render_template, session, url_for, flash, redirect
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=("GET", "POST"))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = "请输入用户名！"
        elif not password:
            error = "请输入密码！"

        if error is None:
            try:
                db.execute("INSERT INTO user (username, password) VALUES (?, ?)"
                           , (username, generate_password_hash(password)),
                           )
                db.commit()
            except db.IntegrityErrorError:
                error = f"用户{username}已经注册了！"
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


# 登录蓝图
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if user is None:
            error = '无法找到输入的用户名'
        elif not check_password_hash(user['password'], password):
            error = '输入的密码不正确'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('classis.index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")

    if not user_id:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id, )
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('classis.index'))




