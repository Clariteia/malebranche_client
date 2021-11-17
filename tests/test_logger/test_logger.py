import unittest

from malebranche.client.logger.logger import Logger


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        logger = Logger
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
