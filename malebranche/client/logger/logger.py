from __future__ import annotations

import logging

from malebranche.client.context import ContextManager
from malebranche.client.logger.filter import MalebrancheLogFilter
from malebranche.client.logger.http_avro_handler import HttpAvroHandler


class Logger:
    def __init__(self, module: str, context: ContextManager, level=logging.DEBUG):
        self.logger: logging.Logger = self.create(module, context, level)

    def create(self, module: str, context, level=logging.DEBUG) -> logging.Logger:
        logging.basicConfig()
        logger = logging.getLogger(__name__)
        if logger.hasHandlers():
            logger.handlers.clear()
            logger.filters.clear()

        network_handler = HttpAvroHandler(host="localhost:5000", url="/logs", method="POST")
        logger.addHandler(network_handler)
        old_level = logger.getEffectiveLevel()
        logger.addFilter(MalebrancheLogFilter(context=context))
        logger.setLevel(level)
        logger.propagate = True

        return logger
