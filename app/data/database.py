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
            user = {
                "tg_id": record[0].get("fields").get("tg_id", "unknown"),
                "username": record[0].get("fields").get("username", "unknown"),
                "firstname": record[0].get("fields").get("firstname", "unknown"),
                "password": record[0].get("fields").get("password", "unknown")
            }
            return user

    def user_is_created(self, user_username):
        is_created = self.search("username", user_username)
        if is_created:
            return True
        else:
            return False

    def auth(self, username, password):
        if username and password:
            username_check = (self.get_user(username).get("username") == username)
            password_check = (self.get_user(username).get("password") == password)
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
