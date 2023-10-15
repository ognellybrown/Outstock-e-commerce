from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError #validations to ensure our password and register data is valid 
from market.models import User

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators= [Length(min=2, max=20), DataRequired()])
    email_address = StringField(label="Email address", validators = [Email(), DataRequired()])
    password1 = PasswordField(label = "Enter password", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label = "Confirm password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = "Register now")


    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data). first()
        if user:
            raise ValidationError('Username Already Exists, please try a different username')

    def validate_username(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data). first()
        if user:
            raise ValidationError('Email Address Already Exists, please try a different Email')

class LoginForm(FlaskForm):
    username = StringField(label= "Enter Username", validators=[Length(min=2, max=20), DataRequired()])
    password = PasswordField(label= "Enter Password", validators=[Length(min=2, max=20), DataRequired()]) 
    submit = SubmitField(label = "LOGIN NOW")
