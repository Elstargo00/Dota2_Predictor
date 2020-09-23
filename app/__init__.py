import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/elstargo/ML/Dota2 Predictor/dota2.db'

db = SQLAlchemy(app)


from . import routes