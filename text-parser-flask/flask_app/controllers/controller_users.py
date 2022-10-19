from flask_app import app, bcrypt
from flask import redirect, request, session, render_template
from flask_app.models.model_users import User


@app.route("/register", methods=["POST"])
def create_user():
    valid = User.validate_registration(request.form)
    if not valid:
        return redirect("/")

    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    session["uuid"] = User.create(user_data)
    return redirect("/dashboard")


@app.route("/login", methods=["POST"])
def login_user():
    user = User.validate_login(request.form)
    if not user:
        return redirect("/")
    session["uuid"] = user.id
    return redirect("/dashboard")


@app.route("/user/account")
def show_my_trees():
    user = User.get_one({"id": session["uuid"]})
    # visitors = User.get_joined_trees({"id": session["uuid"]})
    return render_template("components/tree_show_mine.html", user=user)


@app.route("/logout")
def logout_user():
    session.pop("uuid")
    return redirect("/")
