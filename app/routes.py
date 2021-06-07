from app import app, db
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask import render_template, redirect, url_for

@app.get('/')
def home():
    return render_template("index.html")

@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return form.data
    return render_template("login.html", form=form)

@app.route('/register', methods = ["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(name=form.name.data, email=form.email.data, password=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)
