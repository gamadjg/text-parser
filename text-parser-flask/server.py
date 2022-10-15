from flask_app import app
from flask_app.controllers import controller_routes


str1 = "I went downstairs, then left the house."
str2 = "I descended upon the first floor, and ejected myself from the inside of the house D:"


if __name__ == "__main__":
    app.run(debug=True)
