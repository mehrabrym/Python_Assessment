import unittest
from unittest import mock

from my_offers import get_offers


class test_errors(unittest.TestCase):
    def test_429_first(self):
        print("Test 1 - Testing for error 429 on the first request.")
        response = mock.Mock()
        response.status_code = 429
        response.content = "CONTENT"
        get_offers(response, 0)
        print("Test 1 complete.")

    def test_429_second(self):
        print("Test 2 - Testing for error 429 on the second request.")
        response = mock.Mock()
        response.status_code = 429
        response.content = "CONTENT"
        get_offers(response, 1)
        print("Test 2 complete.")

    def test_500_first(self):
        print("Test 3 - Testing for error 500.")
        response = mock.Mock()
        response.status_code = 500
        response.content = "CONTENT"
        get_offers(response, 0)
        print("Test 3 complete.")

if __name__ == '__main__':
    unittest.main()
