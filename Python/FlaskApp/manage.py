#!/usr/bin/env python
from app.main.database.db import initialize_db
from flask import Flask
from app.main.service.auth import *
from UserLogin import UserLogin
from flask_login import LoginManager, login_user
from werkzeug.security import check_password_hash
from forms import LoginForm
from admin.admin import admin
from flask_restful import Api
from app.main.controller.auth_api import PostApiView, LoginApi, auth_api
from flask_jwt_extended import create_access_token, JWTManager

app = Flask(__name__)

app.secret_key = "fdsjffjhjksnfknckjsdnckjdsn"

api = Api(app)

app.config["MONGODB_SETTINGS"] = "mongodb://localhost/first_mongo_db"
app.config.from_object(__name__)

initialize_db(
    app
)  # Run the function after app and config init. End of the file works well.
# app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=1)

jwt = JWTManager(app)


login_manager = LoginManager(app)
login_manager.login_view = "login"
# login_manager.login_message = "" #show when redirect to login
# login_manager.login_message_category = "warning"
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(auth_api, url_prefix="/api/auth/")


app.add_url_rule("/", view_func=index)
app.add_url_rule("/about", view_func=about)
app.add_url_rule("/profile/<username>/", view_func=get_profile)
app.add_url_rule("/profile", view_func=profile)
app.add_url_rule("/feedback", methods=["GET", "POST"], view_func=get_feedback)
app.add_url_rule("/register", methods=["GET", "POST"], view_func=register)
app.add_url_rule("/logout", view_func=logout)

app.add_url_rule("/book_info", view_func=get_book)
app.add_url_rule("/add_post", methods=["GET", "POST"], view_func=add_post)
app.add_url_rule("/home", view_func=home_page)
app.add_url_rule("/login_with_cookies", view_func=login_with_cookies)
app.add_url_rule("/logout_with_cookies", view_func=logout_with_cookies)

api.add_resource(PostApiView, "/api/posts/")
api.add_resource(LoginApi, "/api/login/")

client = app.test_client()


@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id)


@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect("profile")

    form = LoginForm()
    if form.validate_on_submit():  # if was post method and successfull
        user = Users.objects(email=request.form["email"]).first()
        if user and check_password_hash(user.psw, form.psw.data):
            userlogin = UserLogin().create(user)
            rm = form.remember.data
            login_user(userlogin, remember=rm)
            return redirect(request.args.get("next") or url_for("profile"))

        flash("Неверная пара логин/пароль", "error")

    return render_template("login.html", title="Авторизация", form=form)

    # if request.method == "POST":
    #     user = Users.objects(email=request.form["email"]).first()
    #     if user and check_password_hash(user.psw, request.form["psw"]):
    #         userlogin = UserLogin().create(user)
    #         rm = True if request.form.get('remainme') else False
    #         login_user(userlogin, remember=rm)
    #         return redirect(request.args.get("next") or url_for("profile"))
    #         # if we redirected from page where login_required and we need to log in
    #         # afte we log in we redirect to page from that we came here

    #     flash("Неверная пара логин/пароль", "error")
    # return render_template("login.html", title="Login")



# class SQLUser(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)

#     def get_token(self, expire_time=24):

#         expire_delta = datetime.timedelta(expire_time)
#         token = create_access_token(identity=self.id, expires_delta=expire_delta)
#         return token


if __name__ == "__main__":
    app.run(debug=True)
