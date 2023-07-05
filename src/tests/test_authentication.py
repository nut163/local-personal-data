import unittest
from src.middleware import authentication
from src.models import User
from src.services import UserService
from src.utils import encryption

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()
        self.user = User('testuser', 'testpassword')
        self.encrypted_password = encryption.encrypt(self.user.password)
        self.user_service.create_user(self.user.username, self.encrypted_password)

    def test_authenticate_valid_user(self):
        result = authentication.authenticate(self.user.username, self.user.password)
        self.assertTrue(result)

    def test_authenticate_invalid_user(self):
        result = authentication.authenticate('invaliduser', 'invalidpassword')
        self.assertFalse(result)

    def tearDown(self):
        self.user_service.delete_user(self.user.username)

if __name__ == '__main__':
    unittest.main()