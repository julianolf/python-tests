from __future__ import annotations

from dataclasses import dataclass, field
from sqlite3 import Cursor
from typing import Optional
from uuid import uuid4


@dataclass
class Person:
    name: str
    age: int
    key: str = field(default_factory=lambda: str(uuid4()))

    def create(self, db: Cursor) -> None:
        sql = "INSERT INTO person (key, name, age) VALUES (?, ?, ?)"
        db.execute(sql, (self.key, self.name, self.age))

    @classmethod
    def get(cls, key: str, db: Cursor) -> Optional[Person]:
        sql = "SELECT key, name, age FROM person WHERE key = ?"
        res = db.execute(sql, (key,))
        data = res.fetchone()

        if data:
            return Person(key=data[0], name=data[1], age=data[2])

    @classmethod
    def all(cls, db: Cursor) -> Optional[Person]:
        sql = "SELECT key, name, age FROM person"
        res = db.execute(sql)

        return [Person(key=k, name=n, age=a) for k, n, a in res.fetchall()]
