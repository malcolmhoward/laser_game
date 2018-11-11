from typing import Generator, Tuple


class Path:
    def __init__(self, rate):
        self._rate = rate

    def data(self) -> Generator[Tuple[int, int], None, None]:
        ...

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        ...
