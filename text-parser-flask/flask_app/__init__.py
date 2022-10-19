from flask import Flask
from flask_app.middleware.jaccard_distances import jaccard_similarity
import os

app = Flask(__name__)
app.secret_key = "L33333333TM3333333111111111111N!"
# bcrypt = Bcrypt(app)
DATABASE = os.getenv("DATABASE")
app.secret_key = os.getenv("SECRET_KEY")
