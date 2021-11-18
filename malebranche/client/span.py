from contextvars import (
    ContextVar,
)

from .context import (
    ContextManager,
)
from .logger import (
    Logger,
)

SPANS_TREE = ContextVar("malebranche.spans")


class Span:
    def __init__(self):
        self.logger = None
        self.is_root = False
        self.token = None
        self.context = None

    def __enter__(self):
        try:
            self.context: ContextManager = SPANS_TREE.get()
        except LookupError:
            self.is_root = True
            self.context: ContextManager = ContextManager()
            self.token = SPANS_TREE.set(self.context)
        else:
            self.context.add_child_process()
            SPANS_TREE.set(self.context)

        self.logger = Logger(__name__, self.context, "INFO")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.is_root:
            SPANS_TREE.reset(self.token)
        else:
            self.context.remove_child()
        # logger.setLevel(old_level)
