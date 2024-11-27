import unittest
from DAL.api_client import ApiClient

class TestApiClient(unittest.TestCase):
    
    def setUp(self):
        self.api_client = ApiClient()
    
    def test_get_posts(self):
        posts = self.api_client.get_posts()
        self.assertIsInstance(posts, list)
        self.assertGreater(len(posts), 0)
    
    def test_get_users(self):
        users = self.api_client.get_users()
        self.assertIsInstance(users, list)
        self.assertGreater(len(users), 0)

if __name__ == "__main__":
    unittest.main()
