from src.services.UserService import UserService
from src.utils.webhook import trigger_webhook
from src.utils.encryption import encrypt_data

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def create_user(self, user_data):
        encrypted_data = encrypt_data(user_data)
        user = self.user_service.create_user(encrypted_data)
        trigger_webhook('user_created', user)
        return user

    def get_user(self, user_id):
        user = self.user_service.get_user(user_id)
        return user

    def update_user(self, user_id, user_data):
        encrypted_data = encrypt_data(user_data)
        user = self.user_service.update_user(user_id, encrypted_data)
        trigger_webhook('user_updated', user)
        return user

    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        trigger_webhook('user_deleted', user_id)