import tracemalloc
from tracemalloc import Snapshot


class Memory:
    def __init__(self):
        self.snapshot: Snapshot = None

    def start(self):
        tracemalloc.start()

    def stop(self):
        self.snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()

    def print(self):
        for stat in self.snapshot.statistics('lineno'):
            print(stat)
