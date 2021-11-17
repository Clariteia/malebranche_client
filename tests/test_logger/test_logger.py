import unittest
from logging import INFO

from malebranche.client.context import ContextManager
from malebranche.client.logger.logger import Logger


class TestLogger(unittest.TestCase):
    def setUp(self) -> None:
        context = ContextManager()
        self.logger = Logger(__name__, context)

    def test_info(self):
        with self.assertLogs(__name__, level=INFO):
            self.logger.info("test message")


if __name__ == '__main__':
    unittest.main()
