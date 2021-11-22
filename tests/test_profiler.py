import unittest
from time import (
    sleep,
)

from malebranche.client.profiler import (
    Profiler,
)


class TestProfiler(unittest.TestCase):
    def setUp(self) -> None:
        self.profiler = Profiler()

    def test_start(self):
        self.profiler.start()

    def test_stop(self):
        self.profiler.start()
        self.profiler.stop()

    def test_print(self):
        self.profiler.start()
        for i in range(10):
            sleep(0.001)
        self.profiler.stop()
        self.profiler.print()


if __name__ == "__main__":
    unittest.main()
