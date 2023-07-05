import unittest
from src.utils.api import Api

class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = Api()

    def test_get_request(self):
        response = self.api.get('https://jsonplaceholder.typicode.com/posts/1')
        self.assertEqual(response.status_code, 200)

    def test_post_request(self):
        data = {'title': 'foo', 'body': 'bar', 'userId': 1}
        response = self.api.post('https://jsonplaceholder.typicode.com/posts', data)
        self.assertEqual(response.status_code, 201)

    def test_put_request(self):
        data = {'id': 1, 'title': 'foo', 'body': 'bar', 'userId': 1}
        response = self.api.put('https://jsonplaceholder.typicode.com/posts/1', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_request(self):
        response = self.api.delete('https://jsonplaceholder.typicode.com/posts/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()