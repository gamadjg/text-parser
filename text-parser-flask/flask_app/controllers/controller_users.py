from flask_app import app, bcrypt
from flask import redirect, request, session, render_template
from flask_app.models.model_users import User


@app.route("/register")
def register_user_show():
    return render_template("components/user_registration.html")


@app.route("/register", methods=["POST"])
def create_user_process():
    valid = User.validate_registration(request.form)
    if not valid:
        return redirect("/register")

    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    session["uuid"] = User.create(user_data)
    return redirect("/")


@app.route("/login")
def login_user_show():
    return render_template("components/user_login.html")


@app.route("/login", methods=["POST"])
def login_user_process():
    user = User.validate_login(request.form)
    if not user:
        return redirect("/login")
    session["uuid"] = user.id
    return redirect("/")


# -----------------------------------------------------------DASHBOARD----------------
@app.route("/user/dashboard")
def user_dashboard_show():
    user = User.get_one({"id": session["uuid"]})
    return render_template("components/dashboard.html", user=user)


# -----------------------------------------------------------ACCOUNT------------------


@app.route("/user/account")
def user_account_show():
    return render_template("components/account.html")


# @app.route("/user/account")
# def show_my_trees():
#     user = User.get_one({"id": session["uuid"]})
#     # visitors = User.get_joined_trees({"id": session["uuid"]})
#     return render_template("components/tree_show_mine.html", user=user)


@app.route("/logout")
def logout_user():
    session.pop("uuid")
    return redirect("/")
