from airtable import Airtable

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
            "password": password,
        }

        return self.insert(fields=user)

    def get_user(self, user_username):
        record = self.search("username", user_username)
        if record:
            fields = record[0].get("fields")
            user = {
                "tg_id": fields.get("tg_id", "unknown"),
                "username": fields.get("username", "unknown"),
                "firstname": fields.get("firstname", "unknown"),
                "password": fields.get("password", "unknown")
            }
            return user

    def user_is_created(self, user_username):
        is_created = self.search("username", user_username)
        if is_created:
            return True
        else:
            return False

    def auth(self, username, password):
        user = self.get_user(username)
        if username and password:
            username_check = (user.get("username") == username)
            password_check = (user.get("password") == password)
            if username_check and password_check:
                return True
            else:
                return False

    def get_user_id(self, user_username):
        return self.get_user(user_username).get("tg_id")

    def get_username(self, user_username):
        return self.get_user(user_username).get("username")

    def get_firstname(self, user_username):
        return self.get_user(user_username).get("firstname")

    def get_password(self, user_username):
        return self.get_user(user_username).get("password")
