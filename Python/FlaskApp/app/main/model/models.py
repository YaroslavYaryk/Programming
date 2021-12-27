import datetime
from flask_mongoengine import MongoEngine

db = MongoEngine()


class Book(db.Document):
    title = db.StringField(max_length=60)
    text = db.StringField()
    # pub_date = db.DateTimeField(default=datetime.datetime.now)


class Users(db.Document):
    name = db.StringField(max_length=160)
    email = db.StringField(max_length=160)
    psw = db.StringField(max_length=300)
    pub_date = db.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"Users({self.name}, {self.psw})"
