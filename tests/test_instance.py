import unittest

from malebranche.client.instance import (
    get_logger,
)


class TestInstance(unittest.TestCase):
    def test_root_logger(self):
        with get_logger() as logger:
            pass


if __name__ == "__main__":
    unittest.main()
