import unittest
from src.utils.webhook import Webhook

class TestWebhook(unittest.TestCase):

    def setUp(self):
        self.webhook = Webhook()

    def test_trigger_webhook(self):
        response = self.webhook.trigger('test_event', {'data': 'test_data'})
        self.assertEqual(response.status_code, 200)

    def test_invalid_event(self):
        with self.assertRaises(Exception):
            self.webhook.trigger('invalid_event', {'data': 'test_data'})

    def test_invalid_payload(self):
        with self.assertRaises(Exception):
            self.webhook.trigger('test_event', 'invalid_payload')

if __name__ == '__main__':
    unittest.main()