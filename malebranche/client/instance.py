import contextvars
from contextlib import contextmanager

from .parsers import LoggerParser

_EXECUTION_LOG_CONTEXT = contextvars.ContextVar("malebranche.log", default=None)
_EXECUTION_TRACER_CONTEXT = contextvars.ContextVar("malebranche.tracer", default=None)


class Malebranche(object):
    __slots__ = "_host", "_port", "_service_name"

    def __init__(self, service_name: str, host: str, port: int):
        self._host = host
        self._port = port
        self._service_name = service_name

    @contextmanager
    def logger(self, level="INFO"):
        context = _EXECUTION_LOG_CONTEXT.get()
        if context is not None:
            log = LoggerParser(level, parent=context)
        else:
            log = LoggerParser(level)
        yield log
        log.send()

    @contextmanager
    def tracer(self):
        ...

    def system(self):
        ...
