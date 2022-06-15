from ex07 import settings


class Odd:
    def __init__(self) -> None:
        self.value = 0

    def next(self) -> int:
        self.value += 1

        while self.value % 2 == 0:
            self.value += 1

        return self.value


def package_info() -> str:
    return f"{settings.NAME} v{settings.VERSION}"
