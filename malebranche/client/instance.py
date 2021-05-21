import contextvars
from contextlib import contextmanager

from malebranche.client.manager import ContextManager
from malebranche.client.parsers import LoggerParser

_EXECUTION_LOG_CONTEXT = contextvars.ContextVar("malebranche.log")
_EXECUTION_TRACER_CONTEXT = contextvars.ContextVar("malebranche.tracer", default=None)

@contextmanager
def get_logger():
    try:
        context: ContextManager = _EXECUTION_LOG_CONTEXT.get()
        context.add_child_process()
        _EXECUTION_LOG_CONTEXT.set(context)
        is_root = False
    except LookupError:
        is_root = True
        context: ContextManager = ContextManager()
        token = _EXECUTION_LOG_CONTEXT.set(
            context
        )
    try:
        yield LoggerParser(context=context)
    finally:
        if is_root:
            _EXECUTION_LOG_CONTEXT.reset(token)

