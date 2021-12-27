from app.main.model.models import Book, Users
from flask_restful import Resource
from flask import jsonify, request, make_response
import datetime
import jwt
from flask import Blueprint
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash
from bson.objectid import ObjectId
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)

auth_api = Blueprint("auth_api", __name__)
arr = []


class PostApiView(Resource):
    def get(self):
        books = Book.objects.all()
        result = [
            {"id": str(book.id), "title": book.title, "text": book.text}
            for book in books
        ]
        return jsonify(result)

    def post(self):
        new_one = request.get_json()

        Book(title=new_one["title"], text=new_one["text"]).save()
        books = Book.objects.all()
        result = [
            {"id": str(book.id), "title": book.title, "text": book.text}
            for book in books
        ]
        return jsonify(result)

    def put(self):

        new_one = request.get_json()
        Book.objects.get(title="cool story").update(**new_one)
        # Book(title=new_one["title"], text=new_one["text"]).save()
        books = Book.objects.all()
        result = [
            {"id": str(book.id), "title": book.title, "text": book.text}
            for book in books
        ]
        return jsonify(result)

    def delete(self):
        new_one = request.get_json()

        Book.objects.get(title=new_one["title"], text=new_one["text"]).delete()
        books = Book.objects.all()
        result = [
            {"id": str(book.id), "title": book.title, "text": book.text}
            for book in books
        ]
        return jsonify(result)


class LoginApi(Resource):
    def post(self):
        from manage import app

        auth = request.get_json()

        if auth and check_password_hash(
            Users.objects.filter(name=auth["username"]).first().psw, auth["password"]
        ):
            user = Users.objects.filter(name=auth["username"]).first()
            token = jwt.encode(
                {
                    "user_id": str(user.id),
                    "user": auth["username"],
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
                },
                app.config["SECRET_KEY"],
            )
            refresh = create_refresh_token(identity=str(user.id), expires_delta=datetime.timedelta(minutes=30))

            return jsonify(
                {
                    "user": {
                        "username": user.name,
                        "access": token.decode("UTF-8"),
                        "refresh": refresh
                    }
                }
            )

        return make_response(
            "Could not verify",
            401,
            {"WWW-Authenticate": 'Basic realm="Login required"'},
        )


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from manage import app

        token = ""
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return jsonify({"message": "token is missing"}), 403
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"])
            current_user = Users.objects.filter(id=ObjectId(data["user_id"])).first()
        except Exception:
            return jsonify({"message": "tocken is invalid"}), 403
        return f(current_user, *args, **kwargs)

    return decorated


@auth_api.route('/token/refresh', methods=["POST"])
@jwt_required
def refresh_users_token():
    identity = get_jwt_identity()
    access = create_access_token(identity=identity, expires_delta=datetime.timedelta(minutes=40))

    return jsonify({
        'access': access
    })


@auth_api.route("/unprotected")
def unprotected(current_user):
    return jsonify({"massage": "this page anyone can see"})


@auth_api.route("/protected")
@token_required
def protected(current_user):
    return jsonify({"massage": "this page can see only users with valid token"})


@auth_api.route("/users/")
@token_required
def get_users(current_user):
    users = Users.objects.all()
    print(current_user)
    response = {
        "users": [{"username": user.name, "password": user.psw} for user in users]
    }
    return jsonify(response)


@auth_api.route("/users/", methods=["POST"])
def create_users():
    data = request.get_json()
    Users(name=data["name"], psw=generate_password_hash(data["password"])).save()

    return jsonify({"message": "user added successfully"})


@auth_api.route("/users/", methods=["PUT"])
@token_required
def change_cur_user(current_user):
    data = request.get_json()
    current_user.update(**data)

    return jsonify({"message": "user changed successfully"})


@auth_api.route("/users/", methods=["DELETE"])
@token_required
def delete_cur_user(current_user):
    print(f"current_user - {current_user}")
    current_user.delete()

    return jsonify({"message": "user deleted successfully"})


