"""
Dummy module to mimic `boto3` package just for the sake of
the tests without the need to install any external dependency.
"""
from typing import Any


class Client:
    def put_object(self, *args, **kwargs) -> None:
        pass

    def send_message(self, *args, **kwargs) -> None:
        pass

    def publish(self, *args, **kwargs) -> None:
        pass


def client(_: str) -> Any:
    return Client()
