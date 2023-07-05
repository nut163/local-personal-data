```python
from src.models.User import User
from src.database.userQueries import UserQueries
from src.utils.encryption import encrypt_password, check_password

class UserService:
    def __init__(self):
        self.user_queries = UserQueries()

    def create_user(self, username, password, email):
        encrypted_password = encrypt_password(password)
        user = User(username, encrypted_password, email)
        self.user_queries.insert_user(user)

    def get_user(self, username):
        user = self.user_queries.get_user(username)
        return user

    def update_user(self, username, password=None, email=None):
        user = self.get_user(username)
        if password:
            user.password = encrypt_password(password)
        if email:
            user.email = email
        self.user_queries.update_user(user)

    def delete_user(self, username):
        self.user_queries.delete_user(username)

    def authenticate_user(self, username, password):
        user = self.get_user(username)
        if user and check_password(password, user.password):
            return user
        return None
```