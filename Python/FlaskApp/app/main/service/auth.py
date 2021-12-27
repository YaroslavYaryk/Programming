from flask import (
    render_template,
    url_for,
    request,
    flash,
    redirect,
    session,
    abort,
    make_response,
)
from app.main.model.models import Book, Users
from flask_login import login_required, current_user, logout_user
from werkzeug.security import generate_password_hash
from forms import RegisterForm


# @login_required
def index():
    lister = [1, 2, 3, 4]
    if session.get("visits"):
        session["visits"] += 1
    else:
        session["visits"] = 1
    return render_template(
        "index.html", visits=session.get("visits"), title="Site", lister=lister,
        books=Book.objects.all()
    )


@login_required
def about():
    return render_template("about.html", title="about")


def get_profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)
    return f"this is user {username}"


def get_feedback():

    if request.method == "POST":
        if len(request.form.get("username")) > 3:
            flash("Succesfully sent", category="success")
        else:
            flash("some problems came out", category="error")
        print(request.form["username"])
    return render_template("feedback.html")


def page_not_found(error):
    return render_template("not_found.html", title="about")


@login_required
def profile():
    return f"""<a href="{url_for('logout')}">Выйти из профиля</a>
                user info: {current_user.get_id()}"""


def register():
    res = 0

    form = RegisterForm()
    if form.validate_on_submit():
        hash = generate_password_hash(form.psw.data)
        if not Users(email=form.email.data):
            res = Users(
                name=form.name.data, email=form.email.data, psw=hash
            ).save()
        if res:
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for("login"))
        else:
            flash("Ошибка при добавлении в БД", "error")

    return render_template(
        "registration.html", title="Регистрация", form=form
    )

    # if request.method == "POST":
    #     session.pop("_flashes", None)
    #     if (
    #         len(request.form["name"]) > 4
    #         and len(request.form["email"]) > 4
    #         and len(request.form["psw"]) > 4
    #         and request.form["psw"] == request.form["psw2"]
    #     ):
    #         hash = generate_password_hash(request.form["psw"])
    #         if not Users(email=request.form["email"]):
    #             res = Users(
    #                 name=request.form["name"], email=request.form["email"], psw=hash
    #             ).save()
    #         if res:
    #             flash("Вы успешно зарегистрированы", "success")
    #             return redirect(url_for("login"))
    #         else:
    #             flash("Ошибка при добавлении в БД", "error")
    #     else:
    #         flash("Неверно заполнены поля", "error")
    # return render_template(
    #     "registration.html", title="Registration", user=Users.objects()
    # )


def logout():
    logout_user()
    flash("You successfully logged out")
    return redirect(url_for("login"))


def get_book():
    # Book(title="Simple todo A", text="12345678910").save()
    book = Book.objects()
    return render_template("book_info.html", book=book)


def add_post():
    # Book(title="Simple todo A", text="12345678910").save()
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = Book(title=request.form["name"], text=request.form["post"]).save()
            if not res:
                flash("Ошибка добавления статьи", category="error")
            else:
                flash("Статья добавлена успешно", category="success")
                return redirect(url_for("get_book"))
        else:
            flash("Ошибка добавления статьи", category="error")

    return render_template("add_post.html", title="Добавление статьи")


def home_page():
    response = make_response(render_template("book_info.html"))

    response.headers["Content-Type"] = "text/plain"
    response.headers["Server"] = "FLASK_APP"

    return response


def login_with_cookies():

    log = ""
    if request.cookies.get("Logged"):
        log = request.cookies.get("Logged")

    response = make_response(f"Logged :  {log}")
    response.set_cookie("Logged", "yes")
    return response


def logout_with_cookies():
    response = make_response(f"You're unlogged now")
    response.set_cookie("Logged", "", 0)
    return response
