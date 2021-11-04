
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'fefb31dfbcd71a07b447bad70ae3d4d34ab1e73932a6f72437a9a629665d7025'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////session.db'

from .routes import index, home, signout
