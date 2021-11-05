import logging

from malebranche.client.context import (
    ContextManager,
)
from malebranche.client.parsers import (
    SystemParser,
)


class MalebrancheLogFilter(logging.Filter):
    __slots__ = "_context"

    def __init__(self, context: ContextManager):
        logging.Filter.__init__(self)
        self._context = context

    def filter(self, record: logging.LogRecord) -> bool:
        record.process = self._context.process["process"]
        if self._context.process["parent"] is not None:
            record.parent = self._context.process["parent"]

        sys = SystemParser(host="localhost:5000", url="/logs").updateStack()
        record.sys = sys

        return True
