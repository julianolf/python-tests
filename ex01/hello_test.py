import unittest

from . import hello


class HelloTest(unittest.TestCase):
    def test_message(self):
        expected = "Hello world!"

        message = hello.message()

        self.assertEqual(message, expected)

    def test_message_with_name(self):
        expected = "Hello Joe!"

        message = hello.message("Joe")

        self.assertEqual(message, expected)
