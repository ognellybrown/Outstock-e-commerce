from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label="Username")
    email_address = StringField(label="Enter address")
    password = PasswordField(label = "Enter password")
    submit = SubmitField(label = "Register now")