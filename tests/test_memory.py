import unittest

from malebranche.client.memory import (
    Memory,
)


class TestMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.memory = Memory()

    def test_start(self):
        self.memory.start()

    def test_stop(self):
        self.memory.stop()

    def test_print(self):
        self.memory.start()
        l = [i for i in range(1000)]
        d = {i: i for i in range(1000)}
        self.memory.stop()
        self.memory.print()


if __name__ == "__main__":
    unittest.main()
