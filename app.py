
from datetime import datetime
from flask import Flask, flash, jsonify, redirect, render_template, request, session
# from flask_session import session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mail import Mail, Message
from forms import ContactForm


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Import env variables
app.config.from_object("config")


app.config["MAIL_SERVER"] = "smtppro.zoho.eu"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USERNAME"] = 'contact@mugsoc.me'
app.config["MAIL_PASSWORD"] = app.config["ZOHO_PWD"]
app.config["MAIL_DEBUG"] = True
app.config["MAIL_SUPPRESS_SEND"] = False
app.config["TESTING"] = False
app.config["MAIL_DEFAULT_SENDER"] = ("MugSoc Customer Support", "contact@mugsoc.me")


mail = Mail(app)
def send_message(name, sender, message, subject=""):
    msg = Message(f"Subject text: {subject}", recipients=[sender])
    msg.body = f"Test msg sent at {datetime.now()}\n\n{message}"
    mail.send(msg)
    print("Message sent")

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
        send_message(request.form.get("name"),
                            request.form.get("email"),
                            request.form.get("message"))
        return "Form posted."
    
    elif request.method == "GET":
        return render_template("contact.html", form=form)

@app.route("/cart")
def cart():
    print("hi")
    return render_template("cart.html")