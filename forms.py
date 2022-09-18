from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms import validators, ValidationError

class ContactForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired("Please enter your name.")])
    email = StringField("Email", [validators.InputRequired("Please enter your email address."), validators.Email("Please enter your email addres.")])
    message = TextAreaField("Message", [validators.InputRequired("Please enter your message")])
    submit = SubmitField("Send")