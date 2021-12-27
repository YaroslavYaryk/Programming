from app.main.model.models import Users
from flask_login import (
    UserMixin,
)  # provide is_authenticated , is active and ia_aninymous


class UserLogin(UserMixin):
    def fromDB(self, user_id):
        self.__user = Users.objects(id=user_id).first()
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user.id)
