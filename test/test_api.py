import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_api_comment_new_missing_fields(self):
        response = self.app.post('/api/comment/new', json={})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'ERROR')
        self.assertIn('Missing required fields', data['message'])

    def test_api_comment_list_not_found(self):
        response = self.app.get('/api/comment/list/123')
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], 'NOT-FOUND')
        self.assertIn('Content_id 123 not found', data['message'])

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
