from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SECRET_KEY'] = '0655599bde2ff7c83b0f63c0'
db = SQLAlchemy(app)
app.app_context().push()

from market import routes