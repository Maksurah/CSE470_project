from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '622f17cec408f3ad47f9c598'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///self_dev.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from self_dev import routes, models
