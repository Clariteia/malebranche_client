import logging
from contextvars import ContextVar

from .logger import Logger
from .context import ContextManager

SPANS_TREE = ContextVar("malebranche.spans")


class Span:
    def __init__(self, logger):
        self.logger = logger
        self.is_root = False

    def __enter__(self):
        try:
            context: ContextManager = SPANS_TREE.get()
        except LookupError:
            self.is_root = True
            context: ContextManager = ContextManager()
            token = SPANS_TREE.set(context)
        else:
            context.add_child_process()
            SPANS_TREE.set(context)

        self.logger = Logger(__name__, context, "INFO")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.is_root:
            SPANS_TREE.reset(token)
        else:
            context.remove_child()
        # logger.setLevel(old_level)
