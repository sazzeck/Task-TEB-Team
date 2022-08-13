from airtable import Airtable

from django.contrib.auth.hashers import make_password

from utils import Config


class AirtableUsers(Airtable):
    def __init__(self):
        super().__init__(
            api_key=Config.AIRTABLE_API_KEY,
            base_id=Config.AIRTABLE_BASE_ID,
            table_name=Config.AIRTABLE_TABLE_NAME,
        )

    def user_create(self, tg_id, username, firstname, password):
        user = {
            "tg_id": tg_id,
            "username": username,
            "firstname": firstname,
            "password": make_password(password),
        }

        return self.insert(fields=user)

    def get_user(self, user_id):
        record = self.search("tg_id", user_id)
        if record:
            user = {
                "tg_id": record[0].get("fields").get("tg_id"),
                "username": record[0].get("fields").get("username"),
                "firstname": record[0].get("fields").get("firstname"),
                "password": record[0].get("fields").get("password")
            }
            return user

    def user_is_created(self, user_id):
        is_created = self.search("tg_id", user_id)
        if is_created:
            return True
        else:
            return False

    def auth(self, username, password):
        if username and password is not None:
            username_check = (self.get_user(username).get("username") == username)
            password_check = (self.get_user(username).get("password") == password)
            if username_check and password_check:
                return {"username": username, "password": password}

    def get_user_id(self, user_username):
        return self.get_user(user_username).get("tg_id")

    def get_username(self, user_username):
        return self.get_user(user_username).get("username")

    def get_firstname(self, user_username):
        return self.get_user(user_username).get("firstname")

    def get_password(self, user_username):
        return self.get_user(user_username).get("password")
