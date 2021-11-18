import logging
from contextlib import (
    contextmanager,
)
from contextvars import (
    ContextVar,
)

from malebranche.client.context import (
    ContextManager,
)
from malebranche.client.logger.logger import (
    Logger,
)
from malebranche.client.parsers import (
    SystemParser,
)
from malebranche.client.span import (
    Span,
)

_EXECUTION_LOG_CONTEXT = ContextVar("malebranche.log")
_EXECUTION_TRACER_CONTEXT = ContextVar("malebranche.tracer", default=None)


@contextmanager
def start_span(level=logging.DEBUG):
    try:
        context: ContextManager = _EXECUTION_LOG_CONTEXT.get()
        context.add_child_process()
        _EXECUTION_LOG_CONTEXT.set(context)
        is_root = False
    except LookupError:
        is_root = True
        context: ContextManager = ContextManager()
        token = _EXECUTION_LOG_CONTEXT.set(context)
    try:
        yield Span().__enter__()
    finally:
        if is_root:
            _EXECUTION_LOG_CONTEXT.reset(token)
        else:
            context.remove_child()
        # logger.setLevel(old_level)


@contextmanager
def get_system(host="localhost:8082", url="/system"):
    system = SystemParser(host="localhost:5000", url="/system")
    try:
        yield system
    finally:
        system.emit()
