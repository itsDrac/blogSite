from app import app
from flask import render_template

@app.get('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")
