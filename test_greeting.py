import unittest
from greeting import make_greeting

class TestGreeting(unittest.TestCase):
    def test_make_greeting(self):
        self.assertEqual(make_greeting("Alice"), "Hello, Alice!")

    def test_empty_name(self):
        self.assertEqual(make_greeting(""), "Hello, !")