from flask import Flask
from flask_bcrypt import Bcrypt

DATABASE = "text_parser_schema"

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "L33333333TM3333333111111111111N!"

# app.secret_key = os.getenv("SECRET_KEY")
