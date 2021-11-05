import contextvars
import logging
from contextlib import (
    contextmanager,
)
from logging.handlers import (
    HTTPHandler,
)

from malebranche.client.context import (
    ContextManager,
)
from malebranche.client.parsers import (
    SystemParser,
)
from malebranche.client.parsers.logger import (
    MalebrancheLogFilter,
)
from malebranche.client.span import (
    Span,
)

_EXECUTION_LOG_CONTEXT = contextvars.ContextVar("malebranche.log")
_EXECUTION_TRACER_CONTEXT = contextvars.ContextVar("malebranche.tracer", default=None)


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

    logging.basicConfig()
    logger = logging.getLogger(__name__)
    if logger.hasHandlers():
        logger.handlers.clear()
        logger.filters.clear()

    network_handler = HTTPHandler(host="localhost:5000", url="/logs", method="POST")
    logger.addHandler(network_handler)
    old_level = logger.getEffectiveLevel()
    logger.addFilter(MalebrancheLogFilter(context=context))
    logger.setLevel(level)
    logger.propagate = True
    try:
        yield Span(logger)
    finally:
        if is_root:
            _EXECUTION_LOG_CONTEXT.reset(token)
        else:
            context.remove_child()
        logger.setLevel(old_level)


@contextmanager
def get_system(host="localhost:8082", url="/system"):
    system = SystemParser(host="localhost:5000", url="/system")
    try:
        yield system
    finally:
        system.emit()
