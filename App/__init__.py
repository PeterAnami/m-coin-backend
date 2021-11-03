
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fefb31dfbcd71a07b447bad70ae3d4d34ab1e73932a6f72437a9a629665d7025'


from .routes import index, home, signout
