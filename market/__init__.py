from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = '0655599bde2ff7c83b0f63c0'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.app_context().push()

from market import routes