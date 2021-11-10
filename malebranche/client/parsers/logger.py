from logging import (
    Filter,
    LogRecord,
)

from malebranche.client.parsers import (
    SystemParser,
)


class MalebrancheLogFilter(Filter):
    __slots__ = "_context"

    def __init__(self, context: dict):
        Filter.__init__(self)
        self._context = context

    def filter(self, record: LogRecord) -> bool:
        record.process = self._context.process["process"]
        if self._context.process["parent"] is not None:
            record.parent = self._context.process["parent"]

        sys = SystemParser(host="localhost:5000", url="/logs").updateStack()
        record.sys = sys

        return True
