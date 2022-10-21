from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "L33333333TM3333333111111111111N!"
DATABASE = "text_parser_schema"

# from flask_app import app
from flask_app.controllers import controller_routes, controller_users
