from __future__ import annotations

import logging

from malebranche.client.context import ContextManager
from .filter import MalebrancheLogFilter
from .http_avro_handler import HttpAvroHandler


class Logger:
    def __init__(self, module: str, context: ContextManager, level=logging.DEBUG):
        self.logger: logging.Logger = self._create_logger(module, context, level)

    def _create_logger(self, module: str, context, level=logging.DEBUG) -> logging.Logger:
        logging.basicConfig()
        logger = logging.getLogger(module)
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

    def info(self, msg: str) -> None:
        self.logger.info(msg)
