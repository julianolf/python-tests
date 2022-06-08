import unittest

from . import calc


class TestAdd(unittest.TestCase):
    def test_add_two_positive_numbers(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_add_two_negative_numbers(self):
        self.assertEqual(calc.add(-1, -2), -3)


class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)


class TestDiv(unittest.TestCase):
    def test_div(self):
        self.assertEqual(calc.div(8, 2), 4)

    def test_division_by_zero_error(self):
        with self.assertRaises(ZeroDivisionError):
            calc.div(1, 0)


class TestMod(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(calc.mod(3, 2), 1)
