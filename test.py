import unittest
import requests
from app import app  # Import your Flask application instance

# Define the base URL of your Flask app
base_url = 'http://127.0.0.1:5000'  # Update the port if your Flask app is running on a different port

class TestAPI(unittest.TestCase):
    def test_get_heroes(self):
        response = requests.get(f'{base_url}/heroes')
        self.assertTrue(response.ok)
        self.assertEqual(response.status_code, 200)
        # Add more test cases...

if __name__ == '__main__':
    unittest.main()
