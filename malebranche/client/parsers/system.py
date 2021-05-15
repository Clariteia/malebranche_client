from collections import namedtuple
import psutil
from fastavro import parse_schema

CPU = namedtuple('CPU', ['num', 'percentage'])
RAM = namedtuple('RAM', ['total', 'available', 'used', 'free', 'percent'])


class SystemParser(object):
    __slots__ = '_schema'

    def __init__(self):
        self._schema = {
            'name': 'SystemInfo',
            'namespace': 'malebranche.system.info',
            'type': 'record',
            'fields': [
                {'name': 'cpu_total', 'type': 'int'},
                {'name': 'cpu_percentage', 'type': 'float'},
                {'name': 'memory_total', 'type': 'long'},
                {'name': 'memory_available', 'type': 'long'},
                {'name': 'memory_used', 'type': 'long'},
                {'name': 'memory_free', 'type': 'long'},
                {'name': 'memory_percentage', 'type': 'float'}
            ]
        }

    def get_data(self):
        memory = psutil.virtual_memory()
        data = [{
            'cpu_total': psutil.cpu_count(),
            'cpu_percentage': psutil.cpu_percent(interval=1, percpu=True),
            'memory_total': memory.total,
            'memory_available': memory.available,
            'memory_used': memory.used,
            'memory_free': memory.free,
            'memory_percentage': memory.percent
        }]
        parsed_schema = parse_schema(self._schema)


