import unittest
from src.models.Activity import Activity
from src.services.ActivityService import ActivityService

class TestActivity(unittest.TestCase):

    def setUp(self):
        self.activity_service = ActivityService()
        self.test_activity = Activity('Test Activity', 'This is a test activity')

    def test_create_activity(self):
        result = self.activity_service.create_activity(self.test_activity)
        self.assertEqual(result.name, 'Test Activity')
        self.assertEqual(result.description, 'This is a test activity')

    def test_get_activity(self):
        self.activity_service.create_activity(self.test_activity)
        result = self.activity_service.get_activity('Test Activity')
        self.assertEqual(result.name, 'Test Activity')
        self.assertEqual(result.description, 'This is a test activity')

    def test_update_activity(self):
        self.activity_service.create_activity(self.test_activity)
        updated_activity = Activity('Updated Activity', 'This is an updated test activity')
        result = self.activity_service.update_activity('Test Activity', updated_activity)
        self.assertEqual(result.name, 'Updated Activity')
        self.assertEqual(result.description, 'This is an updated test activity')

    def test_delete_activity(self):
        self.activity_service.create_activity(self.test_activity)
        self.activity_service.delete_activity('Test Activity')
        result = self.activity_service.get_activity('Test Activity')
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()