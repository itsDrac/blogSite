from app import app
from app.forms import LoginForm, RegisterForm
from flask import render_template

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
        return form.data
    return render_template("register.html", form=form)
