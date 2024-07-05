import sys

from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from project.core.forms.form import LoginForm, SignUpForm
from project.connectors import db, limiter
from project.models import User

core_blueprint = Blueprint(
    'core',
    __name__,
    template_folder='templates'
)


@core_blueprint.route("/")
def landing():
    return render_template("landing.html", title="Flask Stack Template")


@core_blueprint.route("/login", methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('core.dashboard'))
        flash('Invalid username or password')
    return render_template('login.html', form=form, title="Flask Stack Template")


@core_blueprint.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(
            email=form.email.data,
            username=form.username.data,
            password=hashed_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('core.login'))
    return render_template('signup.html', form=form, title="Flask Stack Template")


@core_blueprint.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", title="Flask Stack Template")


@core_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.login'))
