import unittest
from unittest.mock import patch

from ex07 import settings, utils


class TestUtils(unittest.TestCase):
    def test_first_five_odd_numbers(self):
        with patch.object(utils.Odd, "next") as m_next:
            m_next.side_effect = [1, 3, 5, 7, 9]

            odd = utils.Odd()
            self.assertIsInstance(odd, utils.Odd)

            for step in range(1, 6):
                with self.subTest(step=step):
                    number = odd.next()

                    self.assertNotEqual(number % 2, 0)

    def test_package_info(self):
        with patch.multiple(settings, NAME="UTILS", VERSION="1.0.0"):
            expected = "UTILS v1.0.0"
            info = utils.package_info()

            self.assertEqual(info, expected)
