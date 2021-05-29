from collections import (
    namedtuple,
)

import psutil

from malebranche.client.parsers.abc import (
    HttpStreamParser,
)

CPU = namedtuple("CPU", ["num", "percentage"])
RAM = namedtuple("RAM", ["total", "available", "used", "free", "percent"])


class SystemParser(HttpStreamParser):
    def updateStack(self):
        memory = psutil.virtual_memory()
        self.stack = {
            "cpu_total": psutil.cpu_count(),
            "cpu_percentage": psutil.cpu_percent(interval=1, percpu=True),
            "memory_total": memory.total,
            "memory_available": memory.available,
            "memory_used": memory.used,
            "memory_free": memory.free,
            "memory_percentage": memory.percent,
        }
        return self.stack
