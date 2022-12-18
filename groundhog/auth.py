from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
)
from werkzeug.security import check_password_hash, generate_password_hash

from groundhog.models import Users, db
from groundhog.helpers import error

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=["GET", "POST"])
def register():
    """Register the user"""

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if username is None or username == "":
            return error("No user name found!")

        if password is None or password == "":
            return error("No password found!")

        if confirmation is None or confirmation == "":
            return error("No password confirmation found!")

        if password == confirmation:
            hash = generate_password_hash(
                request.form.get("password"),
                method="pbkdf2:sha256",
                salt_length=8,
            )

            user = Users(username, hash, email)
            db.session.add(user)
            db.session.commit()

            return redirect("/")
    else:
        return render_template("auth/register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Log user in
    CS50 Problem Set 9 Flask
    """

    # Forget any previous user
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return error("Missing username", 403)

        elif not request.form.get("password"):
            return error("Missing password", 403)

        user = db.session.execute(
            db.select(Users).filter_by(username=username)
        ).one()

        if len(user) != 1 or not check_password_hash(
            user[0].hash, request.form.get("password")
        ):
            return error("invalid username or password", 403)

        session["user_id"] = user[0].id
        return redirect("/")
    else:
        return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    """Log user out"""
    session.clear()

    return redirect("/")
