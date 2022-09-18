
from datetime import datetime
from flask import Flask, flash, jsonify, redirect, render_template, request, session
# from flask_session import session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mail import Mail, Message
from forms import ContactForm

import requests

# Configure application
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Import API keys
app.config.from_object("config")

def send_simple_message(name, sender, message, subject=""):
            return requests.post(
                "https://api.mailgun.net/v3/sandboxed6f16b686514f3b95e5f8513d301aa3.mailgun.org/messages",
                auth=("api", app.config["MAILGUN_APIKEY"]),
                data={"from": f"{name} <{sender}>",
                    "to": ["yfdwf.mugsoctest@inbox.testmail.app"],
                    "subject": subject,
                    "text": message})


# app.config["MAIL_SERVER"] = "smtp-mail.outlook.com"
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_USE_SSL"] = True
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = 'contact@example.com'
# app.config["MAIL_PASSWORD"] = 'your-password'

# mail = Mail(app)


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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template("contact.html", form=form)
        send_simple_message(request.form.get("name"),
                            request.form.get("email"),
                            request.form.get("message"))
        return "Form posted."
    
    elif request.method == "GET":
        return render_template("contact.html", form=form)

@app.route("/cart")
def cart():
    print("hi")
    return render_template("cart.html")


