import logging
import unittest

from .custom_types import *


class TestAssertionMethods(unittest.TestCase):
    def test_equality_between_basic_types(self):
        a = 2 + 2
        b = 2 * 2
        c = 2 // 2

        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_truthy(self):
        boolean = True

        self.assertTrue(boolean)
        self.assertFalse(not boolean)

    def test_identity(self):
        a = Bool.TRUE
        b = Bool.TRUE
        c = Bool.FALSE

        self.assertIs(a, b)
        self.assertIsNot(a, c)

    def test_nullability(self):
        info = {"name": "John"}

        self.assertIsNone(info.get("age"))
        self.assertIsNotNone(info.get("name"))

    def test_items_in_collections(self):
        t = (1, 2, 3)  # tuple
        l = [4, 5, 6]  # list
        s = {7, 8, 9}  # set
        d = {"foo": "bar"}  # dict

        self.assertIn(2, t)
        self.assertIn(4, l)
        self.assertIn(9, s)
        self.assertIn("foo", d)
        self.assertIn("bar", d.values())
        self.assertNotIn(4, t)

    def test_object_class(self):
        person = Person()
        student = Student()

        self.assertIsInstance(person, Person)
        self.assertIsInstance(student, Person)
        self.assertNotIsInstance(student, Alien)

    def test_equality_between_collections(self):
        dict_one = {"one": 1, "two": 2, "three": 3}
        dict_two = {"three": 3, "one": 1, "two": 2}

        self.assertDictEqual(dict_one, dict_two)
        self.assertSetEqual({"a", "b"}, {"b", "a"})
        self.assertListEqual([1, 2], [1, 2])
        self.assertTupleEqual((0, 0), (0, 0))

        # invocados por assertEqual por padrão

        self.assertEqual(dict_one, dict_two)

    def test_numeric_precision(self):
        number = 1 / 3

        self.assertAlmostEqual(number, 0.333, places=3)
        self.assertNotAlmostEqual(number, 0.3)  # (round(number, ndigits=7) - 0.3) == 0

    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            2 / 0

        with self.assertRaisesRegex(ValueError, r"^invalid literal .* 'abc'$"):
            int("abc")

    def test_logs(self):
        log = logging.getLogger("test")

        with self.assertLogs(log, level="ERROR") as ctx:
            log.error("BOOM!")

        self.assertEqual(ctx.output, ["ERROR:test:BOOM!"])

    def test_multiple_values_at_once(self):
        even_numbers = (2, 4, 6, 8)

        for number in even_numbers:
            with self.subTest(number=number):
                self.assertEqual(number % 2, 0)
