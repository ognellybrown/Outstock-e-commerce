from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired #validations to ensure our password and register data is valid 


class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators= [Length(min=2, max=20), DataRequired()])
    email_address = StringField(label="Enter address", validators = [Email(), DataRequired()])
    password1 = PasswordField(label = "Enter password", validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label = "Confirm password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label = "Register now")