from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
from flask_app.models import model_trees as trees
import re

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE users.email = %(email)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result:
            return False
        user = User(result[0])
        return user

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        user = User(results[0])
        return user

    @staticmethod
    def validate_login(data) -> bool:
        is_valid = True
        if len(data["email"]) < 1:
            is_valid = False
            flash("email cannot be empty", "err_email_login")
        elif not EMAIL_REGEX.match(data["email"]):
            is_valid = False
            flash("Invalid email address", "err_email_login")
        if len(data["password"]) < 8:
            is_valid = False
            flash("Incorrect password", "err_password_login")
        if is_valid:
            potential_user = User.get_one_by_email({"email": data["email"]})
            if not potential_user:
                is_valid = False
                flash("Email not found", "err_email_login")
            else:
                if not bcrypt.check_password_hash(
                    potential_user.password, data["password"]
                ):
                    is_valid = False
                    flash("Incorrect password", "err_password_login")
                else:
                    session["uuid"] = potential_user.id
            return potential_user
        return is_valid

    @staticmethod
    def validate_registration(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            is_valid = False
            flash(
                "First species must be at least 2 characters",
                "err_first_name_registration",
            )
        if len(data["last_name"]) < 2:
            is_valid = False
            flash(
                "Last species must be at least 2 characters",
                "err_last_name_registration",
            )
        if len(data["email"]) < 1:
            is_valid = False
            flash("email cannot be empty", "err_email_registration")
        elif not EMAIL_REGEX.match(data["email"]):
            is_valid = False
            flash("Invalid email address", "err_email_registration")
        else:
            potential_user = User.get_one_by_email({"email": data["email"]})
            if potential_user:
                is_valid = False
                flash("Email already exists", "err_email_registration")
        if len(data["password"]) < 8:
            is_valid = False
            flash(
                "Password must be at least 8 characters",
                "err_password_registration",
            )
        if len(data["confirmation_password"]) < 8:
            is_valid = False
            flash(
                "Confirmation password must be at least 8 characters",
                "err_confirmation_password_registration",
            )
        elif data["password"] != data["confirmation_password"]:
            is_valid = False
            flash(
                "Password and confirmation password do not match",
                "err_confirmation_password_registration",
            )
        return is_valid
