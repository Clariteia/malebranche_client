import unittest
from logging import INFO

from malebranche.client import Logger
from malebranche.client.context import ContextManager


class TestLogger(unittest.TestCase):
    TEST_MODULE = "test_module"

    def setUp(self) -> None:
        context = ContextManager()
        self.logger = Logger(self.TEST_MODULE, context)

    def test_info(self):
        with self.assertLogs(self.TEST_MODULE, level=INFO):
            self.logger.info("Test message")


if __name__ == "__main__":
    unittest.main()
