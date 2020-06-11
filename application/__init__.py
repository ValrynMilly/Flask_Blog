import os
from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='Thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from application import routes
