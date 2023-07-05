import unittest
from src.models.Contact import Contact
from src.services.ContactService import ContactService

class TestContact(unittest.TestCase):

    def setUp(self):
        self.contact_service = ContactService()
        self.test_contact = Contact('John Doe', 'john.doe@example.com', '1234567890')

    def test_create_contact(self):
        result = self.contact_service.create_contact(self.test_contact)
        self.assertEqual(result, True)

    def test_get_contact(self):
        self.contact_service.create_contact(self.test_contact)
        result = self.contact_service.get_contact('john.doe@example.com')
        self.assertEqual(result.name, 'John Doe')

    def test_update_contact(self):
        self.contact_service.create_contact(self.test_contact)
        updated_contact = Contact('John Doe', 'john.doe@example.com', '0987654321')
        result = self.contact_service.update_contact(updated_contact)
        self.assertEqual(result.phone, '0987654321')

    def test_delete_contact(self):
        self.contact_service.create_contact(self.test_contact)
        result = self.contact_service.delete_contact('john.doe@example.com')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()