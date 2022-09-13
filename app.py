
from datetime import datetime
from flask import Flask, flash, jsonify, redirect, render_template, request, session
# from flask_session import session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# 
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# db = SQLAlchemy(app)

# Password hash length
salt_length = 8

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(20), unique=True, nullable=False)
#     password_hash = db.Column(db.String(salt_length), nullable=False)
#     time_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now.strftime("%c"))

#     def __repr__(self):
#         return "<USer %r>" % self.username

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/cart")
def cart():
    print("hi")
    return render_template("cart.html")


