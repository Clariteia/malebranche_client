import typing as t
from datetime import datetime
from malebranche.client.parsers.abc import ParserAbstract


class LoggerParser(ParserAbstract):
    __slots__ = "_level"

    def _set_type(self):
        self._type = "LOG"

    def info(self, message: t.Union[str, int, float, dict, list]):
        self.add_to_stack(date=datetime.now().timestamp(), body=message, level="INFO")

    def warning(self, message: t.Union[str, int, float, dict, list]):
        self.add_to_stack(date=datetime.now().timestamp(), body=message, level="WARN")

    def debug(self, message: t.Union[str, int, float, dict, list]):
        self.add_to_stack(date=datetime.now().timestamp(), body=message, level="DEBUG")

    def error(self, message: t.Union[str, int, float, dict, list]):
        self.add_to_stack(date=datetime.now().timestamp(), body=message, level="ERROR")


