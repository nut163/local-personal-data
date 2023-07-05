import unittest
from src.models.User import User
from src.services.UserService import UserService

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()
        self.test_user = User('test_user', 'test_password')

    def test_create_user(self):
        result = self.user_service.create_user(self.test_user)
        self.assertEqual(result, True)

    def test_get_user(self):
        self.user_service.create_user(self.test_user)
        result = self.user_service.get_user('test_user')
        self.assertEqual(result.username, 'test_user')

    def test_update_user(self):
        self.user_service.create_user(self.test_user)
        self.user_service.update_user('test_user', 'new_password')
        result = self.user_service.get_user('test_user')
        self.assertEqual(result.password, 'new_password')

    def test_delete_user(self):
        self.user_service.create_user(self.test_user)
        result = self.user_service.delete_user('test_user')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()