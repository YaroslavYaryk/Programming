from flask import Blueprint
from flask import render_template, url_for, request, flash, redirect, session
from app.main.model.models import Users

admin = Blueprint(
    "admin", __name__, template_folder="templates", static_folder="static"
)


def login_admin():
    session["admin_logged"] = 1


@admin.route("/")
def index():
    if not isLogged():
        return redirect(url_for(".login"))

    return render_template(
        "admin/index.html", title="Админ-панель", users=Users.objects.all()
    )


@admin.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form["user"] == "admin" and request.form["psw"] == "admin":
            login_admin()
            return redirect(url_for(".index"))  # point means that we redirect to
            # index in this blueprint
        else:
            flash("Неверная пара логин/пароль", "error")

    return render_template("admin/login.html", title="Админ-панель")


def isLogged():
    return True if session.get("admin_logged") else False


def logout_admin():
    session.pop("admin_logged", None)


@admin.route("/logout", methods=["POST", "GET"])
def logout():
    if not isLogged():
        return redirect(url_for(".login"))

    logout_admin()

    return redirect(url_for(".login"))
