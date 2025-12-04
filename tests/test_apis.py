import requests
import unittest


class TestAPIs(unittest.TestCase):
    def setUp(self):
        self.response = requests.get("http://127.0.0.1:5000/hello")

    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_response_data_message(self):
        self.assertEqual(self.response.json()["message"], "Hello World!")

    def tearDown(self):
        return super().tearDown()
