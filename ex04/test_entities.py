import sqlite3
import unittest

from . import entities

con = None
cur = None


def setUpModule():
    global con, cur
    con = sqlite3.connect(":memory:")
    cur = con.cursor()


def tearDownModule():
    global con
    con.close()


class TestPerson(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cur.execute("CREATE TABLE person (key TEXT, name TEXT, age INTEGER)")

    @classmethod
    def tearDownClass(cls) -> None:
        cur.execute("DROP TABLE person")

    def setUp(self) -> None:
        self.people = (
            ("30468e09-1d16-4a06-aa45-e90f1f1f5194", "John", 24),
            ("20fac853-4b50-4aa0-a9fb-bac11d852e0f", "Mary", 42),
        )

        cur.executemany(
            "INSERT INTO person (key, name, age) VALUES (?, ?, ?)",
            self.people,
        )

    def tearDown(self) -> None:
        cur.execute("DELETE FROM person")

    def test_all_return_two_people(self):
        result = entities.Person.all(cur)

        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(p, entities.Person) for p in result))

    def test_get_return_person(self):
        key, name, age = self.people[0]

        result = entities.Person.get(key, cur)

        self.assertIsInstance(result, entities.Person)
        self.assertEqual(result.key, key)
        self.assertEqual(result.name, name)
        self.assertEqual(result.age, age)

    def test_create_new_person(self):
        person = entities.Person(name="Alex", age=18)
        person.create(cur)

        result = entities.Person.get(person.key, cur)

        self.assertIsInstance(result, entities.Person)
        self.assertEqual(result.key, person.key)
        self.assertEqual(result.name, person.name)
        self.assertEqual(result.age, person.age)
